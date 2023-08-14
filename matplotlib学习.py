import numpy as np
import matplotlib.pyplot as plt

#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x=np.linspace(-np.pi,np.pi,30,endpoint=True)  #生成一个数组,-Π到+Π的范围,一共30个数据点
C=np.cos(x)
S=np.sin(x)

plt.title('正弦余弦函数')               #命名
plt.plot(x,C,color='red',marker='*',linewidth=1.0,label="cos")    #绘图函数,plt.plot(x, y, format_string, **kwargs) 参数为x轴数据,y轴数据,图像格式
plt.plot(x,S,color='blue',linewidth='2.0',label="sin")  #设置线宽和图例
plt.legend(loc='upper left')#图片左上角图例,内容为plot()函数中的label
plt.xlim(-4.0, 4.0)#设置x轴上下限
plt.ylim(-1.5,1.5)#设置y轴上下限
plt.xticks(np.linspace(-4,4,9,endpoint=True))#x轴上的数字标记,从-4到+4,均分为9个点
plt.yticks(np.linspace(-1,1,5,endpoint=True))#y轴上的数字标记,从-1到+1,均分为5个点

ax = plt.gca()#获取坐标轴,top,bottom,left,right
ax.spines['right'].set_color('none')#将上 右两条坐标轴颜色设置为无色
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data',0))#移动坐标轴位置
ax.spines['left'].set_position(('data',0))

plt.savefig("C:\pythonProject1\picture.png",dpi=100)#参数为文件地址,分辨率
#图片保存,应该在show()函数前保存,不然就是保存为空白,图像在show()函数后重新打离开空白画板
plt.show()
