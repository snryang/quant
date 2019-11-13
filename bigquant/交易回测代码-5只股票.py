# 回测引擎：每日数据处理函数，每天执行一次
def bigquant_run(context, data):
    #获取当日日期
    today = data.current_dt
    today_date = data.current_dt.strftime('%Y-%m-%d')
    
    current_stock = [] # 当前持仓  
    current_stopdays_stock = [] # 固定天数卖出列表    
    current_stopwin_stock = []  # 止盈列表
    current_stoploss_stock = [] # 止损列表
    cash_for_sell = 0 # 当日卖出现金

    equities = {e.symbol: p for e, p in context.portfolio.positions.items() if p.amount>0}    
    if len(equities)>0:
        for sid in equities:            
            symbol = context.symbol(sid)            
            position = equities[sid]
            stock_market_price=data.current(symbol,'price')  #当前市场价
            stock_cost=position.cost_basis  #持仓成本价

            # 固定天数卖出
            if today-position.last_sale_date>=datetime.timedelta(2) and data.can_trade(symbol) and not context.has_unfinished_sell_order(equities[sid]):
                context.order_target_percent(symbol, 0)
                current_stopdays_stock.append(sid)
                cash_for_sell += position.amount * stock_market_price
                continue            

            # 止盈 赚20% 且为可交易状态
            if stock_market_price/stock_cost-1 >= 0.15  and data.can_trade(symbol) and not context.has_unfinished_sell_order(equities[sid]):
                context.order_target_percent(symbol,0)
                current_stopwin_stock.append(sid)
                cash_for_sell += position.amount * stock_market_price
                continue

            # 止损 亏5% 且为可交易状态
            if stock_market_price/stock_cost-1 <= -0.05 and data.can_trade(symbol) and not context.has_unfinished_sell_order(equities[sid]):   
                context.order_target_percent(symbol,0)     
                current_stoploss_stock.append(sid)
                cash_for_sell += position.amount * stock_market_price
                continue
            
            current_stock.append(sid)

    if len(current_stopdays_stock)>0:
        print(today_date,'固定天数卖出列表',current_stopdays_stock)
    if len(current_stopwin_stock)>0:
        print(today_date,'止盈股票列表',current_stopwin_stock)
    if len(current_stoploss_stock)>0:
        print(today_date,'止损股票列表',current_stoploss_stock)

    cash_for_buy = context.portfolio.cash + cash_for_sell  #买入股票 可用现金    
    #单只股标最大仓位金额
    max_cash_per_instrument = context.portfolio.portfolio_value * context.max_cash_per_instrument


    # 按日期过滤得到今日的预测数据
    ranker_prediction = context.ranker_prediction[context.ranker_prediction.date == today_date]

    current_buy_stock = []
    
    for index, row in ranker_prediction.iterrows():
        instrument = row['instrument']
        if len(current_stock) + len(current_buy_stock) > 5:
            break
        if instrument in current_stock:
            continue
        if instrument in current_stoploss_stock:
            continue
        if not data.can_trade(context.symbol(instrument)):
            continue
        # 评分太低，当天不买
        if row['score']<1:
            break
       
        cash = min(max_cash_per_instrument,cash_for_buy)
        price = data.current(context.symbol(instrument), 'price')  # 最新价格
        stock_num = np.floor(cash/price/100)*100  # 向下取整
        context.order(context.symbol(instrument), stock_num) # 整百下单
        cash_for_buy = cash_for_buy - stock_num * price       
        current_buy_stock.append(instrument)
        if cash_for_buy < 10000:
            break
    if len(current_buy_stock)>0:
        print(today_date,'买入股票',current_buy_stock)


# 回测引擎：初始化函数，只执行一次
def bigquant_run(context):
    # 加载预测数据
    context.ranker_prediction = context.options['data'].read_df()


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
    context.max_portfolio_value = 0 #帐户最大市值 用于计算回撤
    context.stop_day = 0 #暂停N天不买入股票
    context.stock_buy_weights = 0.2  #每日购买股票能使用的最大资金比例


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
