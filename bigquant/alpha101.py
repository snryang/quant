Alpha_1=where(mean(amount_0,20)<volume_0,((-1*ts_rank(abs(delta(close_0,7)),60))*sign(delta(close_0,7))),-1)
Alpha_2=rank(ts_argmax(signedpower(where(close_0/shift(close_0,1)-1<0,std(close_0/shift(close_0,1)-1<0,20),close_0),2),5))-0.5
Alpha_3=-1*correlation(rank(delta(log(volume_0),2)),rank(((close_0-open_0)/open_0)),6)
Alpha_4=-1*correlation(rank(open_0),rank(volume_0),10)   
Alpha_5=-1*ts_rank(rank(low_0),9)
Alpha_6=rank((open_0-(sum(amount_0/volume_0*adjust_factor_0,10)/10)))*(-1*abs(rank((close_0-amount_0/volume_0*adjust_factor_0))))
Alpha_7=-1*correlation(open_0,volume_0,10) 
Alpha_8=where(mean(amount_0,20)<volume_0,((-1*ts_rank(abs(delta(close_0,7)),60))*sign(delta(close_0,7))),-1)  

Alpha_9=(-1*rank(((sum(open_0,5)*sum(close_0/shift(close_0,1)-1,5))-delay((sum(open_0,5)*sum(close_0/shift(close_0,1)-1,5)),10))))

Alpha_10=where(0<ts_min(delta(close_0,1),5),delta(close_0,1),where(ts_max(delta(close_0,1),5)<0,delta(close_0,1),-1*delta(close_0,1)))

Alpha_11=rank(where(0<ts_min(delta(close_0,1),4),delta(close_0,1),where(ts_max(delta(close_0,1),4)<0,delta(close_0,1),-1*delta(close_0,1))))

Alpha_12=(rank(ts_max((amount_0/volume_0*adjust_factor_0-close_0),3))+rank(ts_min((amount_0/volume_0*adjust_factor_0-close_0),3)))*rank(delta(volume_0,3))

Alpha_13=sign(delta(volume_0,1))*(-1*delta(close_0,1))

Alpha_14=-1*rank(covariance(rank(close_0),rank(volume_0),5))

Alpha_15=(-1*rank(delta(close_0/shift(close_0,1)-1,3)))*correlation(open_0,volume_0,10)

Alpha_16=-1*sum(rank(correlation(rank(high_0),rank(volume_0),3)),3)

Alpha_17=-1*rank(covariance(rank(high_0),rank(volume_0),5))

Alpha_18=((-1*rank(ts_rank(close_0,10)))*rank(delta(delta(close_0,1),1)))*rank(ts_rank((volume_0/mean(amount_0,20)),5))

Alpha_19=-1*rank(((std(abs((close_0-open_0)),5)+(close_0-open_0))+correlation(close_0,open_0,10)))

Alpha_20=(-1*sign(((close_0-delay(close_0,7))+delta(close_0,7))))*(1+rank((1+sum(close_0/shift(close_0,1)-1,250))))

Alpha_21=((-1*rank((open_0-delay(high_0,1))))*rank((open_0-delay(close_0,1))))*rank((open_0-delay(low_0,1)))

Alpha_22=where(sum(close_0,8)/8+stddev(close_0,8)<sum(close_0,2)/2,-1,where(mean(close_0,2)<mean(close_0,8)-std(close_0,8),1,where((1<volume_0/mean(amount_0,20)) |(volume_0/mean(amount_0,20)==1),1,-1)))

Alpha_23=-1*(delta(correlation(high_0,volume_0,5),5)*rank(std(close_0,20)))

Alpha_24=where(sum(high_0,20)/20<high_0,-1*delta(high_2,0),0)

Alpha_25=where((delta(mean(close_0,100),100)/delay(close_0,100)<0.05)  |(delta(mean(close_0,100),100)/delay(close_0,100)==0.05) ,-1*(close_0-ts_min(close_0,100)),-1*delta(close_0,2))

Alpha_26=rank(-1*(close_0/shift(close_0,1)-1)*mean(amount_0,20)*amount_0/volume_0*adjust_factor_0*(high_0-close_0))

Alpha_27=-1*ts_max(correlation(ts_rank(volume_0,5),ts_rank(high_0,5),5),3)

Alpha_28=where(0.5<rank((sum(correlation(rank(volume_0),rank(amount_0/volume_0*adjust_factor_0),6),2)/2.0)),-1,1)

Alpha_29=scale(correlation(mean(amount_0,20),low_0,5)+(high_0+low_0)*0.5-close_0)   

Alpha_30=min(product(rank(rank(scale(log(sum(ts_min(rank(rank((-1*rank(delta((close_0-1),5))))),2),1))))),1),5)+ts_rank(delay((-1*shift(close_0,1)/close_0-1),6),5)

Alpha_31=((1.0-rank(((sign((close_0-delay(close_0,1)))+sign((delay(close_0,1)-delay(close_0,2)))) +sign((delay(close_0,2)-delay(close_0,3))))))*sum(volume_0,5))/sum(volume_0,20)

Alpha_32=(rank(rank(rank(decay_linear((-1*rank(rank(delta(close_0,10)))),10))))+rank((-1*delta(close_0,3))))+sign(scale(correlation(mean(amount_0,20),low_0,12)))

Alpha_33=scale(((sum(close_0,7)/7)-close_0))+20*scale(correlation(amount_0/volume_0*adjust_factor_0,delay(close_0,5),230))

Alpha_34=rank((-1*((1-(open_0/close_0)))))

Alpha_35=rank(((1-rank((std(close_0/shift(close_0,1),2)/stddev(close_0/shift(close_0,1)-1,5))))+(1-rank(delta(close_0,1))))) 

Alpha_36=ts_rank(volume_0,32)*(1-ts_rank(((close_0+high_0)-low_0),16))*(1-ts_rank(close_0/shift(close_0,1)-1,32))

Alpha_37=((((2.21*rank(correlation((close_0-open_0),delay(volume_0,1),15)))+(0.7*rank((open_0-close_0))))+(0.73*rank(ts_rank(delay((-1*close_0/shift(close_0,1)-1),6),5))))+rank(abs(correlation(amount_0/volume_0*adjust_factor_0,mean(amount_0,20),6))))+(0.6*rank((((sum(close_0,200)/200)-open_0)*(close_0-open_0)))) 

Alpha_38=rank(correlation(delay((open_0-close_0),1),close_0,200))+rank((open_0-close_0))

Alpha_39=(-1*rank(ts_rank(close_0,10)))*rank((close_0/open_0))

Alpha_40=((-1*rank((delta(close_0,7)*(1-rank(decay_linear((volume_0/mean(amount_0,20)),9))))))*(1 +rank(sum(close_0/shift(close_0,1),250))))

Alpha_41=((-1*rank(std(high_0,10)))*correlation(high_0,volume_0,10))

Alpha_42=(((high_0*low_0)**0.5)-amount_0/volume_0*adjust_factor_0)

Alpha_43=(rank((amount_0/volume_0*adjust_factor_0-close_0))/rank((amount_0/volume_0*adjust_factor_0+close_0)))

Alpha_44=(ts_rank((volume_0/mean(amount_0,20)),20)*ts_rank((-1*delta(close_0,7)),8))

Alpha_45=(-1*correlation(high_0,rank(volume_0),5))

Alpha_46=(-1*((rank((sum(delay(close_0,5),20)/20))*correlation(close_0,volume_0,2))*rank(correlation(sum(close_0,5),sum(close_0,20),2)))),

Alpha_47=where((0.25<(((delay(close_0,20)-delay(close_0,10))/10)-((delay(close_0,10)-close_0)/10))),-1,where(((((delay(close_0,20)-delay(close_0,10))/10)-((delay(close_0,10)-close_0)/10))<0),1,((-1*1)*(close_0-delay(close_0,1)))))

Alpha_48=(((rank((1/close_0))*volume_0)/mean(amount_0,20))*((high_0*rank((high_0-close_0)))/(sum(high_0,5) /5)))-rank((amount_0/volume_0*adjust_factor_0-delay(amount_0/volume_0*adjust_factor_0,5))) 

Alpha_49=((correlation(delta(close_0,1),delta(delay(close_0,1),1),250)*delta(close_0,1))/close_0)/group_mean(industry_sw_level1_0,((correlation(delta(close_0,1),delta(delay(close_0,1),1),250)*delta(close_0,1))/close_0))/sum(((delta(close_0,1)/delay(close_0,1))**2),250)    

Alpha_50=where(((((delay(close_0,20)-delay(close_0,10))/10)-((delay(close_0,10)-close_0)/10))<(-1*0.1)),1,(close_0-delay(close_0,1))*(-1))   

Alpha_51=(-1*ts_max(rank(correlation(rank(volume_0),rank(amount_0/volume_0*adjust_factor_0),5)),5))

Alpha_52=where((((delay(close_0,20)-delay(close_0,10))/10)-((delay(close_0,10)-close_0)/10))<(-1*0.05),1,-1*(close_0-delay(close_0,1)))

Alpha_53=(((-1*ts_min(low_0,5))+delay(ts_min(low_0,5),5))*rank(((sum(close_0/shift(close_0,1),240)-sum(close_0/shift(close_0,1),20))/220)))*ts_rank(volume_0,5)

Alpha_54=(-1*delta((((close_0-low_0)-(high_0-close_0))/(close_0-low_0)),9))

Alpha_55=((-1*((low_0-close_0)*(open_0**5)))/((low_0-high_0)*(close_0** 5))) 

Alpha_56=-1*correlation(rank(((close_0-ts_min(low_0,12))/(ts_max(high_0,12)-ts_min(low_0,12)))),rank(volume_0),6)

Alpha_57=0-1*(1*(rank((sum(close_0/shift(close_0,1)-1,10)/sum(sum(close_0/shift(close_0,1)-1,2),3)))*rank(((close_0/shift(close_0,1)-1)*market_cap_0)))) 

Alpha_58=(0-(1*((close_0-amount_0/volume_0*adjust_factor_0)/decay_linear(rank(ts_argmax(close_0,30)),2)))) 

Alpha_59=(-1*ts_rank(decay_linear(correlation( amount_0/volume_0*adjust_factor_0/group_mean(industry_sw_level1_0,amount_0/volume_0*adjust_factor_0),volume_0,4),8),5))

Alpha_60=(0-(1*((2*scale(rank(((((close_0-low_0)-(high_0-close_0))/(high_0-low_0))*volume_0))))-scale(rank(ts_argmax(close_0,10))))))

Alpha_61=(rank((amount_0/volume_0*adjust_factor_0-ts_min(amount_0/volume_0*adjust_factor_0,16)))<rank(correlation(amount_0/volume_0*adjust_factor_0,mean(amount_0,180),18)))

Alpha_62=(rank(correlation(amount_0/volume_0*adjust_factor_0,sum(mean(amount_0,20),22),10))<rank(((rank(open_0)+rank(open_0))<(rank(((high_0+low_0)/2))+rank(high_0)))))*-1

Alpha_63=((rank(decay_linear(delta(close_0/group_mean(industry_sw_level1_0,close_0),2),8))-rank(decay_linear(correlation(((amount_0/volume_0*adjust_factor_0*0.318108)+(open_0*(1-0.318108))),sum(mean(amount_0,180),37),14),12)))*-1)

Alpha_64=((rank(correlation(sum(((open_0*0.178404)+(low_0*(1-0.178404))),13),sum(mean(amount_0,20),13),17))<rank(delta(((((high_0+low_0)/2)*0.178404)+(amount_0/volume_0*adjust_factor_0*(1-0.178404))),4)))*-1)

Alpha_65=((rank(correlation(((open_0*0.00817205)+(amount_0/volume_0*adjust_factor_0*(1-0.00817205))),sum(mean(amount_0,60),9),6))<rank((open_0-ts_min(open_0,14))))*-1)

Alpha_66=((rank(decay_linear(delta(amount_0/volume_0*adjust_factor_0,4),7))+ts_rank(decay_linear(((((low_0* 0.96633)+(low_0*(1-0.96633)))-amount_0/volume_0*adjust_factor_0)/(open_0-((high_0+low_0)/2))),11),7))*-1)

Alpha_67=((rank((high_0-ts_min(high_0,2)))**rank(correlation( amount_0/volume_0*adjust_factor_0 /group_mean(industry_sw_level1_0,amount_0/volume_0*adjust_factor_0),mean(amount_0,20)/group_mean(industry_sw_level1_0,mean(amount_0,20)),6)))*-1)

Alpha_68=((ts_rank(correlation(rank(high_0),rank(mean(amount_0,15)),9),14)<rank(delta(((close_0*0.518371)+(low_0*(1-0.518371))),1.06157)))*-1)

Alpha_69=((rank(ts_max(delta(amount_0/volume_0*adjust_factor_0/group_mean(industry_sw_level1_0,amount_0/volume_0*adjust_factor_0),3),5))**ts_rank(correlation(((close_0*0.490655)+(amount_0/volume_0*adjust_factor_0*(1-0.490655))),mean(amount_0,20),5),9))*-1)

Alpha_70=((rank(delta(amount_0/volume_0*adjust_factor_0,1))**ts_rank(correlation(  close_0/group_mean(industry_sw_level1_0,close_0),mean(amount_0,50),18),18))*-1)

Alpha_71=max(ts_rank(decay_linear(correlation(ts_rank(close_0,3),ts_rank(mean(amount_0,180),12),18),4),16),ts_rank(decay_linear((rank(((low_0+open_0)-(amount_0/volume_0*adjust_factor_0 +amount_0/volume_0*adjust_factor_0)))**2),16 ),4))

Alpha_72=(rank(decay_linear(correlation(((high_0+low_0)/2),mean(amount_0,40),9),10)) /rank(decay_linear(correlation(ts_rank(amount_0/volume_0*adjust_factor_0,4),ts_rank(volume_0,19),7),3)))

Alpha_73=(max(rank(decay_linear(delta(amount_0/volume_0*adjust_factor_0,5),3)),ts_rank(decay_linear(((delta(((open_0* 0.147155)+(low_0*(1-0.147155))),2 ) /((open_0* 0.147155)+(low_0*(1-0.147155))))*-1),3),17))*-1)      

Alpha_74=(rank(correlation(close_0,sum(mean(amount_0,30),37),15))<rank(correlation(rank(high_0*0.0261661+amount_0/volume_0*adjust_factor_0*(1-0.0261661)),rank(volume_0),11)))*-1

Alpha_75=rank(correlation(amount_0/volume_0*adjust_factor_0,volume_0,4 ))<rank(correlation(rank(low_0),rank(mean(amount_0,50)),12))

Alpha_76=max(rank(decay_linear(delta(amount_0/volume_0*adjust_factor_0,1),12)),ts_rank(decay_linear(ts_rank(correlation( low_0/group_mean(industry_sw_level1_0,low_0),mean(amount_0,81),8 ),20),17),19))*-1

Alpha_77=min(rank(decay_linear(((((high_0+low_0)/2)+high_0)-(amount_0/volume_0*adjust_factor_0+high_0)),20 )),rank(decay_linear(correlation(((high_0+low_0)/2),mean(amount_0,40),3),6)))

Alpha_78=rank(correlation(sum(((low_0*0.352233)+(amount_0/volume_0*adjust_factor_0*(1-0.352233))),20),sum(mean(amount_0,20),20),7))**rank(correlation(rank(amount_0/volume_0*adjust_factor_0),rank(volume_0),6))

Alpha_79=rank(delta((close_0*0.60733+open_0*(1-0.60733))/ group_mean(industry_sw_level1_0,(close_0*0.60733+open_0*(1-0.60733))),1))<rank(correlation(ts_rank(amount_0/volume_0*adjust_factor_0,4),ts_rank(mean(amount_0,150),9),115))

Alpha_80=(rank(sign(delta((open_0*0.868128+high_0*(1-0.868128))/group_mean(industry_sw_level1_0,(open_0*0.868128+high_0*(1-0.868128))),4)))**ts_rank(correlation(high_0,mean(amount_0,10),5),6))*-1

Alpha_81=(rank(log(product(rank((rank(correlation(amount_0/volume_0*adjust_factor_0,sum(mean(amount_0,10),50),8))**4)),15)))<rank(correlation(rank(amount_0/volume_0*adjust_factor_0),rank(volume_0),5)))*-1

Alpha_82=min(rank(decay_linear(delta(open_0,1.46063),15)),ts_rank(decay_linear(correlation( volume_0/group_mean(industry_sw_level1_0,volume_0),((open_0*0.634196) +(open_0*(1-0.634196))),17),7),13))*-1

Alpha_83=(rank(delay(((high_0-low_0)/(sum(close_0,5)/5)),2))*rank(rank(volume_0)))/(((high_0-low_0)/(sum(close_0,5)/5))/(amount_0/volume_0*adjust_factor_0-close_0))

Alpha_84=signedpower(ts_rank((amount_0/volume_0*adjust_factor_0-ts_max(amount_0/volume_0*adjust_factor_0,15)),20),delta(close_0,5))

Alpha_85=rank(correlation(((high_0*0.876703)+(close_0*(1-0.876703))),mean(amount_0,30),10))**rank(correlation(ts_rank(((high_0+low_0)/2),4),ts_rank(volume_0,10),7))

Alpha_86=(ts_rank(correlation(close_0,sum(mean(amount_0,20),15),6),20)<rank(((open_0+close_0)-(amount_0/volume_0*adjust_factor_0+open_0))))*-1

Alpha_87=max(rank(decay_linear(delta(((close_0*0.369701)+(amount_0/volume_0*adjust_factor_0*(1-0.369701))),2),3)),ts_rank(decay_linear(abs(correlation( mean(amount_0,81) /group_mean(industry_sw_level1_0,mean(amount_0,81)) ,close_0,14)),5),14))*-1

Alpha_88=min(rank(decay_linear(((rank(open_0)+rank(low_0))-(rank(high_0)+rank(close_0))),8)),ts_rank(decay_linear(correlation(ts_rank(close_0,8),ts_rank(mean(amount_0,60),21),8),7),3))

Alpha_89=ts_rank(decay_linear(correlation(((low_0*0.967285)+(low_0*(1-0.967285))),mean(amount_0,10),7),6),4)-ts_rank(decay_linear(delta( amount_0/volume_0*adjust_factor_0/group_mean(industry_sw_level1_0,amount_0/volume_0*adjust_factor_0),3),10),15)

Alpha_90=(rank((close_0-ts_max(close_0,5)))**ts_rank(correlation(mean(amount_0,40)/group_mean(industry_sw_level1_0,mean(amount_0,40)),low_0,5),3))*-1

Alpha_91=(ts_rank(decay_linear(decay_linear(correlation(close_0/group_mean(industry_sw_level1_0,close_0),volume_0,10),16),4),5)-rank(decay_linear(correlation(amount_0/volume_0*adjust_factor_0,mean(amount_0,30),4),3)))*-1

Alpha_92=min(ts_rank(decay_linear(((((high_0+low_0)/2)+close_0)<(low_0+open_0)),15),19),ts_rank(decay_linear(correlation(rank(low_0),rank(mean(amount_0,30)),8),7),7))

Alpha_93=ts_rank(decay_linear(correlation((amount_0/volume_0*adjust_factor_0)/group_mean(industry_sw_level1_0,amount_0/volume_0*adjust_factor_0) ,mean(amount_0,81),17),20),8)/rank(decay_linear(delta(((close_0*0.524434)+(amount_0/volume_0*adjust_factor_0*(1-0.524434))),3),16))

Alpha_94=(rank((amount_0/volume_0*adjust_factor_0-ts_min(amount_0/volume_0*adjust_factor_0,12)))**ts_rank(correlation(ts_rank(amount_0/volume_0*adjust_factor_0,20),ts_rank(mean(amount_0,60),4),18),3))*-1

Alpha_95=rank((open_0-ts_min(open_0,12)))<ts_rank((rank(correlation(sum(((high_0+low_0)/ 2),19),sum(mean(amount_0,40),19),13))**5),12)

Alpha_96=max(ts_rank(decay_linear(correlation(rank(amount_0/volume_0*adjust_factor_0),rank(volume_0),4),4),8),ts_rank(decay_linear(ts_argmax(correlation(ts_rank(close_0,7),ts_rank(mean(amount_0,60),4),4),13),14),13))*-1     

Alpha_97=(rank(decay_linear(delta(((low_0*0.721001)+(amount_0/volume_0*adjust_factor_0*(1-0.721001)))/group_mean(industry_sw_level1_0,(low_0*0.721001)+(amount_0/volume_0*adjust_factor_0*(1-0.721001))),3),20)) -ts_rank(decay_linear(ts_rank(correlation(ts_rank(low_0,8),ts_rank(mean(amount_0,60),17),5),16),16),7))*-1

Alpha_98=rank(decay_linear(correlation(amount_0/volume_0*adjust_factor_0,sum(mean(amount_0,5),26),5),7))-rank(decay_linear(ts_rank(ts_argmin(correlation(rank(open_0),rank(mean(amount_0,15)),21),9),7),8))

Alpha_99=(rank(correlation(sum(((high_0+low_0)/2),20),sum(mean(amount_0,60),20),9)) <rank(correlation(low_0,volume_0,6)))*-1

Alpha_100=-1*(((1.5*scale(rank(((((close_0-low_0)-(high_0-close_0))/(high_0-low_0))*volume_0))/group_mean(industry_sw_level2_0,rank(((((close_0-low_0)-(high_0-close_0))/(high_0-low_0))*volume_0)))))-scale((correlation(close_0,rank(mean(amount_0,20)),5)-rank(ts_argmin(close_0,30)))/group_mean(industry_sw_level2_0,(correlation(close_0,rank(mean(amount_0,20)),5)-rank(ts_argmin(close_0,30))))))*(volume_0/mean(amount_0,20)))

Alpha_101=(close_0-open_0)/((high_0-low_0)+0.001)