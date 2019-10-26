import pandas as pd

df = pd.read_csv('./test.csv') #读取csv文件

df.head(3) # 前3条，默认前5条
df.tail(3) # 后3条,默认后5条


print (help(df.read_csv)) #查看某个函数的帮助文档

df.info() #查看DataFrame数据结构信息
df.index #索引
df.columns #列名
df.dtypes #列的数据结构


#通过字典创建dataframe结构
data = {
    'country':['a','b','c'],
    'population':[10,20,30]
}
df_data = pd.DataFrame(data)

np.nan  #空值

age = df['Age']
age[:5] # 获取Age列前5条数据 Series结构
age.values[:5] # Age列的前5条数据，array结构

type(age)  #查看对象类型

df.set_index('name') #设置name列为索引

age['Allen, Mr. William Henry'] # Series结构 通过索引获取值

df.describe() # 对数值类型的列，获取基本统计特性

### pandas索引
df['Age'] #获取Age列
df[['Age','Fare']] #获取Age Fare列

df.iloc[0] #用position定位，获取第一条数据，返回Series结构
df.iloc[0,5] #返回第一条数据，第6列的值
df.iloc[0:5] #定位前5条数据，返回DataFrame结构
df.iloc[0:5,1:3] #定位前5条数据，返回2，3列

df = df.set_index('Name')
df.loc['Heikkinen, Miss. Laina'] #通过label定位
df.loc['Heikkinen, Miss. Laina','Age']
df.loc['Heikkinen, Miss. Laina',['Age','SibSp']]
df.loc['Heikkinen, Miss. Laina':'Allen, Mr. William Henry',:] #获取二个label之间的数据，取所有列

df.loc['Heikkinen, Miss. Laina','Fare'] = 1000 # 修改索引位置，Fare列的值为1000

df['Fare'] > 40 #返回一个boll类型的Series,Fare>40 为True 否则为False
df[df['Fare'] > 40][:5] #返回Fare列 >40的前5条数据
df[df['Sex'] == 'male'][:5] #返回Sex列等于'male'的前5条数据

df.loc[df['Sex'] == 'male','Age'].mean() #女性年龄平均值
    # df['Sex'] == 'male' 得到一个Bool类型索引
    # df.loc[df['Sex'] == 'male'] 定位到索引的数据
    # df.loc[df['Sex'] == 'male','Age'] 取年龄字段
    # .mean() 求平均值

(df['Age'] > 70).sum() #年龄>70的人数

### groupby函数
df = pd.DataFrame({
    'key':['A','B','C','A','B','C','A','B','C'],
    'data':[0,5,10,5,10,15,10,15,20]
})

df.groupby('key').sum()
df.groupby('key').aggregate(np.mean) #等同上一句代码，传入一个函数，求值

df.groupby('Sex')['Age'].mean() #统计不同性别年龄平均值

### 数值运算
df.corr() #数值相关性
df['Age'].value_counts #统计不同年龄的人数 == groupby年龄 .sum()
df['Age'].value_counts(ascending=True,bins=5) # 数据分5个区间统计

### 对象操作
#### Series结构的增删改查
data=[10,11,12]
index = ['a','b','c']
s = pd.Series(data = data,index=index)
'key' in s # 索引key，在Series中是否存在

s1 = s.copy()
s1.replace(to_replace = 100,value=101,inplace=True) #Series中所有100改为101，inplace是否影响s1
    # 默认inplace = false,不会修改s1
s1.index = ['A','B','C'] #修改Series的索引
s1.rename(index = {'a':'A'},inplace = True) #索引重命名

data = [100,110]
index = ['h','k']
s2 = pd.Series(data = data,index = index)
s3 = s1.append(s2) # 将s1,s2合为一个新的s3

s1.append(s2,ignore_index = True) #s1,s2合并时，忽略原始索引，重新生成int型索引

del s1['A'] #删除索引处数据
s1.drop(['b','d'],inplace=True) #删除索引处数据

#### DataFrame结构的增删改查
data = [[1,2,3],[4,5,6]]
index = ['a','b']
columns = ['A','B','C']

df = pd.DataFrame(data=data,index=index,columns = columns)

df['A']
df.iloc[0]
df.loc['a']
df.loc['a']['A'] = 160
df.index = ['f','g']
'key' in df.index

data = [[1,2,3],[4,5,6]]
index = ['j','k']
columns = ['A','B','C']

df2 = pd.DataFrame(data=data,index=index,columns = columns)
df3 = pd.concat([df,df2],axis=0)
df2['Tang'] = [10,11] #增加一列
df2.loc['c'] = [1,2,3,4] #增加一行

df5.drop(['j'],axis=0,inplace = True) #删除一行数据
del df5['Tang']  #删除一列数据
df5.drop(['A','B','C'],axis = 1,inplace = True) #删除多列数据


### 数据合并
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                    'A': ['A0', 'A1', 'A2', 'A3'], 
                    'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                    'C': ['C0', 'C1', 'C2', 'C3'], 
                    'D': ['D0', 'D1', 'D2', 'D3']})
pd.merge(left,right) # 等同于 pd.merge(left,right,on='key')
pd.merge(left,right,on=['key1','key2']) #merge key1 key2相同的数据
pd.merge(left,right,on=['key1','key2'],how='outer',indicator=True)
pd.merge(left,right,on=['key1','key2'],how='left')
pd.merge(left,right,on=['key1','key2'],how='right') #同sql left join right join

left.join(right,on='Key') # 等同于 pd.merge(left,right)

pd.get_option('display.max_rows')
pd.set_option('display.max_rows') #设置默认输出几条数据
