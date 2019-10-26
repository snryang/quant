import numpy as np

array = np.array([1,2,3,4,5])
array2 = array +1 #数组中所有元素+1
print(type(array2)) # >> class 'numpy.ndarray'

array.shape # >>(5,) 一维数组，5个元素

# ndarray结构，里面所有的元素必须是同一类型，如果不是，会自动的向下进行转换
array.dtype #查看ndarray的元素类型 
array.size 大小

array.fill(0)  # 用0值填充数据
array.ndim # 数据的维度，一维 二维 

array = np.array([[1,2,3],
                    [4,5,6]
                    7,8,9])
array[1,1]      #获取多维数组中的某个值
array[1,1] = 10 #设置多维数组中的某个值
array[1]  # > array([4,5,6])
array[:,1] # > array([2,5,8])
array[0,0:2] # > array([1,2])  获取第一行的前二个元素

array # 普通赋值修改，都是共享底层数据
array.copy()  #拷贝一份数据，避免数据互相影响

array = np.arange(0,100,10) # 0-100 步长10 生成数字
mask = np.array([0,0,0,0,0,1,1,1,1],dtype=bool)
array[mask] # 输出true对应的数据

random_array = np.random.rand(10) #输出10个随机值
mask = random_array > 0.5
random_array[mask]

np.where(random_array > 0.5) # 随机数中大于0.5的值

random_array.astype(np.float32) #转换数据类型

np.sum() #所有数据求合
np.sum(array,axis=0) # ndim==2时 axis 0:X轴相加 1：Y轴相加 ，

array.argmin() # 找最小值索引
array.argmax(axis=0)
array.mean() #平均值
array.std() #标准差
array.var() #方差

array.clip(2,4) #截断，数组中小于2的都设置为2，大于4的都设置为4
array.round(1) #四舍五入到小数点后1位 
np.sort(array,axis=0) #排序
np.argsort(array) # 找排序的索引

np.linspace(0,10,10) # 从0开始，到10结束，找10个数字，10个数字间距一样
np.searchsorted(array,values) # 将values排序插入array

np.lexsort([-1*array[:,0] , array[:,2] ]) #第1列降序 同时第3列升序

array.shape # >> (10,)
array.shape = 2,5 #>将数组改为2行5列

array[np.newaxis,:] #数组增加一个维度

array.transpose() # 将2行5列数组改为2列5行，行列互换
# array.transpose == array.T

np.concatenate((a,b),axis = 0) #数组链接，按维度
# np.concatenate((a,b),axis = 0) == np.vstack((a,b))
# np.concatenate((a,b),axis = 1) == np.hstack((a,b))

a.flatten() # 将多维数据转为一维数据

np.logspace(0,1,5)
np.linspace(-10,10,5)

np.zeros(3) # 构建一维数组3个数，填充为0
np.zeros((3,3)) # 构建二维数据组9个数，填充为0
np.ones(3)    #用1填充
np.ones((3,3))  #用1填充
np.empty(3)  #构建空数组

b = np.zeros_like(a)
b = np.ones_like(a) # 构建和A结构一样的B数组，值填充为1

x = np.array([2,2])
y = np.array([5,5])
np.multiply(x,y) # >> array([10,10])

np.dot(x,y) # 一维数据，内积运算
            # 二维数据，矩阵计算

np.random.rand(3,2) #随机生成3行2列数组 值是从0到1
np.random.randint(10,size=(5,4)) #返回随机整数，左闭右开
np.random.randint(0,10,3) # 0-10之间，取3个随机数

np.random.normal(mu,sigma,10) #构建10个高斯分布结果

np.set_printoptions(precision = 2) #设置np默认打印结果为小数点后2位

np.random.shuffle(array) #洗牌 随机打乱数组顺序

np.random.seed(100) #指定随机种子

np.loadtxt('a.txt') #将数据读取到np 默认空格分割
np.loadtxt('a.txt',delimiter=',',skiprows = 1) # 读取数据不要第一行
np.savetxt('b.txt')

np.save('a.npy',array) # 将np数据结构保存到文件
np.load('a.npy')       # 读取np文件

