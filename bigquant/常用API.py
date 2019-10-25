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
data.can_trade(context.symbol(instrument))

context.order_target_value(sid, weight*cash_for_buy) # 买入


# 加载预测数据
    df = context.options['data'].read_df()

交易对象：https://bigquant.com/docs/develop/modules/trade/context_objects.html

context.order(context.symbol('000001.SZA'), 100) # 下一个市价单
context.order(context.symbol('000001.SZA'), 100, style=MarketOrder()) # 下一个市价单, 功能同上
# 下一个限价单（买入）, 价位应低于市价，价格小于等于10元买入
context.order(context.symbol('000001.SZA'), 100, style=LimitOrder(10.0))
# 下一个止损单（卖出）,价格小于等于10元卖出100股
context.order(context.symbol('000001.SZA'), -100, style=StopOrder(10.0))