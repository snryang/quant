# 预测15天的涨幅

#因子
Alpha_48=(((rank((1/close_0))*volume_0)/mean(amount_0,20))*((high_0*rank((high_0-close_0)))/(sum(high_0,5) /5)))-rank((amount_0/volume_0*adjust_factor_0-delay(amount_0/volume_0*adjust_factor_0,5)))
Alpha_86=(ts_rank(correlation(close_0,sum(mean(amount_0,20),15),6),20)<rank(((open_0+close_0)-(amount_0/volume_0*adjust_factor_0+open_0))))*-1
Alpha_12=(rank(ts_max((amount_0/volume_0*adjust_factor_0-close_0),3))+rank(ts_min((amount_0/volume_0*adjust_factor_0-close_0),3)))*rank(delta(volume_0,3))
a1=std(return_0,10)
a2=std(high_0-low_0,10)/mean(high_0-low_0,10)
a3=ts_argmax(high_0, 10)-ts_argmin(low_0, 10)
a4=ts_argmax(close_0, 10)-ts_argmin(close_0, 10)
a5=avg_turn_3/avg_turn_20
a6=-1*correlation(return_0, turn_0, 20) 