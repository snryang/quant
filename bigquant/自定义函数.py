#标注
#10日内的最高收益

where(
min(shift(close, -10),shift(close, -9),shift(close, -8),shift(close, -7),shift(close, -6),shift(close, -5),shift(close, -4),shift(close, -3),shift(close, -2),shift(close, -1))/shift(open, -1) -1 > -0.01
,max(shift(close, -10),shift(close, -9),shift(close, -8),shift(close, -7),shift(close, -6),shift(close, -5),shift(close, -4),shift(close, -3),shift(close, -2),shift(close, -1))/shift(open, -1)
,0
)

# 计算收益：6日收盘价(作为卖出价格)除以明日开盘价(作为买入价格)
shift(close, -10) / shift(open, -1)



# pd.set_option('display.max_rows',120)
#计算nan值有多少个
df.isna().sum()
adjust_factor_0               0
amount_0                      0
close_0                       0
date                          0
high_0                        0
industry_sw_level1_0          0
instrument                    0
low_0                         0
market_cap_0                  0
open_0                        0
volume_0                      0
Alpha_6                    8257
Alpha_9                   14751
Alpha_30                  10360
Alpha_34                      0
Alpha_35                   4353
Alpha_39                   8257
Alpha_42                      0
Alpha_43                      0
Alpha_55                   6169
Alpha_57                   9313
Alpha_101                     0
Alpha_3                    6521
Alpha_4                    8311
Alpha_12                   2545
Alpha_13                    829
Alpha_14                   3429
Alpha_15                   8257
Alpha_16                   3821
Alpha_17                   3429
Alpha_27                  24609
Alpha_45                   3456
Alpha_48                  19256
Alpha_51                   8556
Alpha_83                   8834
Alpha_31                  19256
Alpha_32                  32017
Alpha_41                   8257
Alpha_44                  41435
Alpha_46                 118467
Alpha_52                    829
Alpha_54                  32880
Alpha_56                  15877
Alpha_60                  14227
Alpha_62                      0
Alpha_66                 685903
Alpha_68                      0
Alpha_73                  20392
Alpha_78                  48704
Alpha_84                  35448
Alpha_86                      0
Alpha_98                  63177
Alpha_85                  58051
Alpha_74                      0
Alpha_75                      0
Alpha_77                  53876
Alpha_81                      0
Alpha_87                 209386
Alpha_88                 850768
Alpha_92                  54858
Alpha_94                 398818
Alpha_95                      0
Alpha_96                3180304
Alpha_99                      0
m:amount                      0
m:high                        0
m:low                         0
m:close                       0
m:open                        0
label                         0
dtype: int64