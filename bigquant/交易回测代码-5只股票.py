# 回测引擎：每日数据处理函数，每天执行一次
def m4_handle_data_bigquant_run(context, data):
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
            stock_market_high=data.current(symbol,'high')  #当前最高价
            stock_market_close=data.current(symbol,'close')  #当前收盘价

            stock_cost=position.cost_basis  #持仓成本价

            # 固定天数卖出
            if today-position.last_sale_date>=datetime.timedelta(2) and data.can_trade(symbol) and not context.has_unfinished_sell_order(equities[sid]):
                context.order_target_percent(symbol, 0)
                current_stopdays_stock.append(sid)
                cash_for_sell += position.amount * stock_market_price
                continue            

            # 止盈 赚15% 且为可交易状态
            if stock_market_price/stock_cost-1 >= 0.15  and data.can_trade(symbol) and not context.has_unfinished_sell_order(equities[sid]):
                context.order_target_percent(symbol,0)
                current_stopwin_stock.append(sid)
                cash_for_sell += position.amount * stock_market_price
                continue

            # 止损 亏8% 且为可交易状态
            if stock_market_price/stock_cost-1 <= -0.08 and data.can_trade(symbol) and not context.has_unfinished_sell_order(equities[sid]):   
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