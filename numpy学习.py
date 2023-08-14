import numpy as np
e=np.empty([3,2],dtype=int)  #创建一个三行两列空数组
print(e,end='\n\n')

a=np.array( [ [1,2,3,4,5],[6,7,8,9,10] ] )  #有一个中括号千万不要少
print(a,end='\n\n\n')

b=np.array( [1.666,2,3,4,5] ,dtype='float' ,copy=False)#转化数据类型,copy默认为True,如果c=b操作,创建副本,对c的操作影响b; 如果False,不会创建副本,对c的操作也影响b

c=b.copy()   #ip不同
#c=b           #ip相同
#c=np.array(b)  #ip不同
print('b:',id(b),'\t','c:',id(c),end='\n\n')

f=[11,22,33,44]
g=np.asarray(f) #任意形式的输入参数，可以是，列表, 列表的元组, 元组, 元组的元组, 元组的列表，多维数组,功能与array相似
print(g)

h=np.linspace(2.4,24,10)  #生成等差数列,参数为,起始点,终止点,总个数
print(h)

i=np.logspace(0,5,6,base=3)   #生成等比数数列,参数分别为 起始点:base的x次方,结束点:base的x平凡,比值
print(i)

j=np.arange(10)
qiepian=slice(2,10,3)    #切片操作,参数  起始点,终止点,步长
print(j[qiepian],end='\n\n')

x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print ("我们的数组是：" )
print (x)
rows = np.array([[0,0],[3,3]])  #行
cols = np.array([[0,2],[0,2]])   #列,分别上下对应,第0行第0列,第0行第2列....又因为本身是二维数组,所以输出也是二维数组
y = x[rows,cols]
print('这个数组的四个角元素是：')
print (y,end='\n\n')


k=np.array([[1,2,3,4,5],[6,7,8,9,10]])  #布尔索引
print(k[k>4],end='\n\n')


l=np.array([[1,2,3],[4,5,6],[7,8,9],[9,10,11],[12,13,14],[15,16,17]])
print(l[ [2,3,-1] ],end='\n\n')     #二维数组索引,也要对应加一个中括号

m=np.array([1,2,3,4,5])
n=np.array([6,7,8,9,10])
print(m*n,end='\n\n')   #广播,两个数组的形状shape必相似,数组对应位置元素参与运算

a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
b = np.array([1,2,3])
print(a+b,end='\n\n')  #不同维度数组广播
