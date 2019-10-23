# 通过positions对象，使用列表生成式的方法获取目前持仓的股票列表
stock_hold_now = {e.symbol: p.amount * p.last_sale_price
                    for e, p in context.perf_tracker.position_tracker.positions.items()} 


#获取帐户可用现金
context.portfolio.cash 

#将标的转化为equity格式
sid = context.symbol(instrument)
#全部卖出股票
context.order_target_percent(sid, 0)


cur_position = context.portfolio.positions[sid].amount # 持仓

#当天是否可以交易
data.can_trade(sid)

context.order_target_value(sid, weight*cash_for_buy) # 买入


# 加载预测数据
    df = context.options['data'].read_df()