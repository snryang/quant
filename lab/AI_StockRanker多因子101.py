    #获取当日日期
    today = data.current_dt
    today_date = data.current_dt.strftime('%Y-%m-%d')

    current_stock = [] # 当前持仓  
    current_stopdays_stock = [] # 固定天数卖出列表    
    current_stopwin_stock = []  # 止盈列表
    current_stoploss_stock = [] # 止损列表    

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
                continue            

            # 止盈 赚15% 且为可交易状态
            if stock_market_price/stock_cost-1 >= 0.15  and data.can_trade(symbol) and not context.has_unfinished_sell_order(equities[sid]):
                context.order_target_percent(symbol,0)
                current_stopwin_stock.append(sid)                
                continue

            # 止损 亏5% 且为可交易状态
            if stock_market_price/stock_cost-1 <= -0.05 and data.can_trade(symbol) and not context.has_unfinished_sell_order(equities[sid]):   
                context.order_target_percent(symbol,0)     
                current_stoploss_stock.append(sid)                
                continue
            
            current_stock.append(sid)

    if len(current_stopdays_stock)>0:
        print(today_date,'固定天数卖出列表',current_stopdays_stock)
    if len(current_stopwin_stock)>0:
        print(today_date,'止盈股票列表',current_stopwin_stock)
    if len(current_stoploss_stock)>0:
        print(today_date,'止损股票列表',current_stoploss_stock)

    cash_for_buy = context.portfolio.cash  #买入股票 可用现金    
    cash_for_buy_max = context.portfolio.portfolio_value * 0.33 #每天最多买33%仓位
    cash_for_buy = min(cash_for_buy,cash_for_buy_max)
    #单只股标最大仓位金额
    max_cash_per_instrument = context.portfolio.portfolio_value * 0.15 #每只股票最多占用15%仓位    

    # 按日期过滤得到今日的预测数据
    ranker_prediction = context.ranker_prediction[context.ranker_prediction.date == today_date]

    current_buy_stock = []
    current_buy_stock_score = []
    for index, row in ranker_prediction.iterrows():
        if cash_for_buy < 5000:            
            break
        instrument = row['instrument']
        if instrument in current_stock:
            continue
        if instrument in current_stoploss_stock:
            continue
        if not data.can_trade(context.symbol(instrument)):
            continue        
        score = row['score']
        cash = min(max_cash_per_instrument,cash_for_buy)        
        price = data.current(context.symbol(instrument), 'price')  # 最新价格        
        stock_num = np.floor(cash/price/100)*100  # 向下取整
        if stock_num == 0:
            continue
        context.order(context.symbol(instrument), stock_num) # 整百下单
        cash_for_buy = cash_for_buy - stock_num * price               
        current_buy_stock.append(instrument)
        current_buy_stock_score.append(score)
        
    if len(current_buy_stock)>0:
        print(today_date,'买入股票',current_buy_stock)
        print(today_date,'股票得分',current_buy_stock_score)