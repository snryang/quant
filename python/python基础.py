
# 在a数组中过滤出在b数组中存在的元素
[ i for i in a if i in b ]
# 在a数组中过滤出在b数组中不存在的元素
[ i for i in a if i not in b ]  

#修改数组中的第3-5个元素
a[2:5] = [13, 14, 15] 

#删除数组中的第3-5个元素
a[2:5] = []

del a[:] #删除整个列表

#数组元素翻转
inputWords=inputWords[-1::-1]

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam') 
print(a) 
print(a - b)     # a 和 b 的差集 
print(a | b)     # a 和 b 的并集 
print(a & b)     # a 和 b 的交集 
print(a ^ b)     # a 和 b 中不同时存在的元素


tuple(s)  #将序列 s 转换为一个元组
list(s)  #将序列 s 转换为一个列表
max(list) # 返回列表元素最大值

range(5) => [0,1,2,3,4
range(5,9) => [5,6,7,8]


把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__()


两个星号 ** 的参数会以字典的形式导入

sum = lambda arg1, arg2: arg1 + arg2

### 列表推导式
[3*x for x in vec]
[[x, x**2] for x in vec]
>>> vec1 = [2, 4, 6]
>>> vec2 = [4, 3, -9]
>>> [x*y for x in vec1 for y in vec2]
[8, 6, -18, 16, 12, -36, 24, 18, -54]
>>> [x+y for x in vec1 for y in vec2]
[6, 5, -7, 8, 7, -5, 10, 9, -3]
>>> [vec1[i]*vec2[i] for i in range(len(vec1))]
[8, 12, -54]
>>> [str(round(355/113, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']

>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
以下实例将3X4的矩阵列表转换为4X3列表：
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


#同时遍历两个或更多的序列，可以使用 zip() 组合：

>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.

#要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数：
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1

#正则表达式分组匹配
    for item in re.finditer(r'@Path\("(?P<method>\S+)"\)',content):
        method = item.group('method')