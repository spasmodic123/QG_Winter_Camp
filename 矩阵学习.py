import numpy as np
import numpy.matlib

a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print(np.dot(a,b),end='\n\n')   #二维数组dot是矩阵乘法,一维dot是对应元素点乘
print(np.vdot(a,b),end='\n\n')             #向量点乘,对应位置元素相乘,结果相加
print((np.inner(a,b)),end='\n\n')          #数组内积.对于二维数组, 1*5+2*6,1*7+2*8,类推. 对于一维数组,相当于一维dot
print(np.matmul(a,b),end='\n\n')           #矩阵乘法


print('========================')
c= np.arange(8).reshape(2,2,2)            #对于三维和二维进行矩阵乘法,将三维里面的每一个二维数组进行矩阵乘法
d = np.arange(4).reshape(2,2)
print(c)
print('============')
print(d)
print('===========')
print(np.matmul(c,d))


e=np.array([[1,2],[3,4]])
f=np.linalg.inv(e)     #输出e的逆矩阵
print(e)
print(f)
print(np.matmul(e,f))   #最终结果受到精度影响


print('===================')
g=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(g)
print( np.array( list(zip(*g)) ) )    #矩阵的转置,先用zip(*数组名),再用list()转换成列表,再用np.arrar转换数组


h=np.array([11,22,33,44,55,66])
np.savez("C:\pythonProject\date.npy.npz",g,h)   #savez()函数一次性存多个数组,存储在npz拓展名文件中
print('读取文件如下:')
i=np.load("C:\pythonProject\date.npy.npz")
print(i['arr_0'],end='\n\n')                #读取
print(i['arr_1'],end='\n\n')


j=np.array([999,888,777,666,555,444])
np.save("C:\pythonProject1\dete1.npy",j)               #save函数存储,储存在npy拓展名文件中
k=np.load("C:\pythonProject1\dete1.npy")
print(j)