# 回测引擎：每日数据处理函数，每天执行一次
def bigquant_run(context, data):
    #获取当日日期
    today_date = data.current_dt.strftime('%Y-%m-%d')
    
    #大盘风控模块，读取风控数据    
    benckmark_risk=context.benckmark_risk.ix[today_date].values[0]

    #当risk为1时，市场有风险，全部平仓，不再执行其它操作
    if benckmark_risk > 0:
        position_all = context.portfolio.positions.keys()
        for i in position_all:
            context.order_target(i, 0)
        print(today_date,'大盘风控止损触发,全仓卖出')
        return
    
    # 按日期过滤得到今日的预测数据
    ranker_prediction = context.ranker_prediction[
        context.ranker_prediction.date == data.current_dt.strftime('%Y-%m-%d')]
    
    # 1. 资金分配
    # 平均持仓时间是hold_days，每日都将买入股票，每日预期使用 1/hold_days 的资金
    # 实际操作中，会存在一定的买入误差，所以在前hold_days天，等量使用资金；之后，尽量使用剩余资金（这里设置最多用等量的1.5倍）
    is_staging = context.trading_day_index < context.options['hold_days'] # 是否在建仓期间（前 hold_days 天）
    cash_avg = context.portfolio.portfolio_value / context.options['hold_days']
    cash_for_buy = min(context.portfolio.cash, (1 if is_staging else 1.5) * cash_avg)
    cash_for_sell = cash_avg - (context.portfolio.cash - cash_for_buy)
    positions = {e.symbol: p.amount * p.last_sale_price
                 for e, p in context.perf_tracker.position_tracker.positions.items()}

    #---------------------------START:止赢止损模块(含建仓期)--------------------
    # 新建当日止赢止损股票列表是为了handle_data 策略逻辑部分不再对该股票进行判断
    current_stopwin_stock=[]
    current_stoploss_stock = []   
    today_date = data.current_dt.strftime('%Y-%m-%d')
    positions_stop={e.symbol:p.cost_basis 
    for e,p in context.portfolio.positions.items()}
    if len(positions_stop)>0:
        for i in positions_stop.keys():
            stock_cost=positions_stop[i]  
            stock_market_price=data.current(context.symbol(i),'price')  
            # 赚15% 且为可交易状态就止盈
            if stock_market_price/stock_cost-1 >= 0.13  and data.can_trade(context.symbol(i)) and not context.has_unfinished_sell_order(i):
                context.order_target_percent(context.symbol(i),0)      
                current_stopwin_stock.append(i)
            # 亏10%并且为可交易状态就止损
            if stock_market_price/stock_cost-1 <= -0.1 and data.can_trade(context.symbol(i)) and not context.has_unfinished_sell_order(i):   
                context.order_target_percent(context.symbol(i),0)     
                current_stoploss_stock.append(i)
        if len(current_stopwin_stock)>0:
            print(today_date,'止盈股票列表',current_stopwin_stock)
        if len(current_stoploss_stock)>0:
            print(today_date,'止损股票列表',current_stoploss_stock)
    #--------------------------END: 止赢止损模块-----------------------------
    
    #--------------------------START：持有固定天数卖出(不含建仓期)---------------
    current_stopdays_stock = [] 
    today = data.current_dt
    today_date = data.current_dt.strftime('%Y-%m-%d')
    # 不是建仓期（在前hold_days属于建仓期）
    if not is_staging:
        equities = {e.symbol: p for e, p in context.portfolio.positions.items() if p.amount>0}
        if len(equities)>0:
            for i in equities:
                sid = equities[i].sid  # 交易标的
                #如果上面的止盈止损已经卖出过了，就不要重复卖出以防止产生空单
                if i in current_stopwin_stock+current_stoploss_stock:
                    continue
                # 今天和上次交易的时间相隔hold_days就全部卖出 datetime.timedelta(context.options['hold_days'])也可以换成自己需要的天数，比如datetime.timedelta(5)
                if today-equities[i].last_sale_date>=datetime.timedelta(5) and data.can_trade(context.symbol(i)) and not context.has_unfinished_sell_order(equities[i]):
                    context.order_target_percent(sid, 0)
                    current_stopdays_stock.append(i)
            if len(current_stopdays_stock)>0:        
                print(today_date,'固定天数卖出列表',current_stopdays_stock)
    #-------------------------------END:持有固定天数卖出--------------------------    
    
    
    # 2. 生成卖出订单：hold_days天之后才开始卖出；对持仓的股票，按机器学习算法预测的排序末位淘汰
    if not is_staging and cash_for_sell > 0:
        equities = {e.symbol: e for e, p in context.perf_tracker.position_tracker.positions.items()}
        instruments = list(reversed(list(ranker_prediction.instrument[ranker_prediction.instrument.apply(
                lambda x: x in equities and not context.has_unfinished_sell_order(equities[x]))])))
        for instrument in instruments:
            #防止多个止损条件同时满足，出现多次卖出产生空单
            if instrument not in current_stopdays_stock+current_stopwin_stock+current_stoploss_stock:
                context.order_target(context.symbol(instrument), 0)
                cash_for_sell -= positions[instrument]
            else:
                cash_for_sell -= positions[instrument]
            if cash_for_sell <= 0:
                break

    # 3. 生成买入订单：按机器学习算法预测的排序，买入前面的stock_count只股票
    buy_cash_weights = context.stock_weights
    buy_instruments_tmp = list(ranker_prediction.instrument)
    #防止卖出后再次买入
    buy_instruments=[k for k in buy_instruments_tmp if k not in current_stopdays_stock+current_stopwin_stock+current_stoploss_stock]
    max_cash_per_instrument = context.portfolio.portfolio_value * context.max_cash_per_instrument
    
    but_stock_count = 0
    for i, instrument in enumerate(buy_instruments):        
        cash = cash_for_buy * 0.2
        if cash > max_cash_per_instrument - positions.get(instrument, 0):
            # 确保股票持仓量不会超过每次股票最大的占用资金量
            cash = max_cash_per_instrument - positions.get(instrument, 0)
        if cash > 0:
            score = ranker_prediction[ranker_prediction['instrument']==instrument].iloc[0]['score']
            if score<0.8:
                break
                
            price = data.current(context.symbol(instrument), 'price')  # 最新价格
            stock_num = np.floor(cash/price/100)*100  # 向下取整
            context.order(context.symbol(instrument), stock_num) # 整百下单
            print(today_date,'购买股票',instrument)
            but_stock_count += 1
        if but_stock_count >= 5:
            break



# 回测引擎：初始化函数，只执行一次
def bigquant_run(context):
    
    # 加载预测数据
    #context.ranker_prediction = context.options['data'].read_df()
    df = context.options['data'].read_df()
    ins= list(df.instrument.unique())
    start = df.date.min()
    end = df.date.max()
    #获取代码的股票名称
    df_name=D.history_data(instruments=ins, start_date=start, end_date=end,fields=['name'])
    df_merge=pd.merge(df,df_name,on=['instrument','date'])
    #过滤掉含有‘退’字的股票
    df_filter=df_merge[~(df_merge.name.str.contains('退'))]
    df_filter=df_filter[~(df_filter.name.str.contains('ST'))]
    context.ranker_prediction = df_filter
    
    
    print(context.ranker_prediction.columns)
    # 系统已经设置了默认的交易手续费和滑点，要修改手续费可使用如下函数
    context.set_commission(PerOrder(buy_cost=0.0003, sell_cost=0.0013, min_cost=5))
    # 预测数据，通过options传入进来，使用 read_df 函数，加载到内存 (DataFrame)
    # 设置买入的股票数量，这里买入预测股票列表排名靠前的5只
    stock_count = 5
    # 每只的股票的权重，如下的权重分配会使得靠前的股票分配多一点的资金，[0.339160, 0.213986, 0.169580, ..]
    # context.stock_weights = T.norm([1 / math.log(i + 2) for i in range(0, stock_count)])
    #改为等权重配置
    context.stock_weights = [1 / stock_count for i in range(0, stock_count)]
    # 设置每只股票占用的最大资金比例
    context.max_cash_per_instrument = 0.2
    context.options['hold_days'] = 5


# 回测引擎：准备数据，只执行一次
def bigquant_run(context):
    #在数据准备函数中一次性计算每日的大盘风控条件相比于在handle中每日计算风控条件可以提高回测速度
    # 多取50天的数据便于计算均值(保证回测的第一天均值不为Nan值)，其中context.start_date和context.end_date是回测指定的起始时间和终止时间
    start_date= (pd.to_datetime(context.start_date) - datetime.timedelta(days=50)).strftime('%Y-%m-%d')     
    benckmark_data=D.history_data(instruments=['000001.SZA'], start_date=start_date, end_date=context.end_date,fields=['close'])
    #计算指数5日涨幅
    benckmark_data['ret5']=benckmark_data['close']/benckmark_data['close'].shift(5)-1
    #计算大盘风控条件，如果5日涨幅小于-5%则设置风险状态risk为1，否则为0
    benckmark_data['risk'] = np.where(benckmark_data['ret5']<-0.04,1,0)
    #修改日期格式为字符串(便于在handle中使用字符串日期索引来查看每日的风险状态)
    benckmark_data['date']=benckmark_data['date'].apply(lambda x:x.strftime('%Y-%m-%d'))
    #设置日期为索引
    benckmark_data.set_index('date',inplace=True)
    #把风控序列输出给全局变量context.benckmark_risk
    context.benckmark_risk=benckmark_data[['risk']]
