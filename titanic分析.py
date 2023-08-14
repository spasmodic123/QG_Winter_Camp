import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']#解决输入中文问题
plt.rcParams['axes.unicode_minus'] = False

train=pd.read_csv(r"C:\Users\changan\Downloads\train.csv")#读取文件
#print(train.info())#查看基本信息

print('-------------------------------------------------------------------------------------------------------------')

survive_rate=train['Survived'].value_counts()#对'Survived'这一列,相同的数据进行计数
print(survive_rate,end='\n\n')

plt.figure(figsize=(6,6))#figure()函数创建空白图像,figsize()函数,对应参数宽和高
plt.pie(survive_rate,autopct='%.2f%%',labels=['死亡','存活'],pctdistance=0.5,labeldistance=0.65,
       shadow=False,explode=[0,0.1],textprops=dict(size=15))
'''pie()函数绘制饼状图,第一个参数为数据,autopct为字符串,保留两位小数加百分号(61.62%),label标签,pct参数为两个字符串的距离
labeldistance参数为两个标签的距离,shadow阴影(可有可无),explode每一块的突出程度,多个饼之间的间隙,textprops标签的格式'''
plt.title('总体生还率')
plt.savefig("survive_rate.png")
plt .show()

print('----------------------------------------------------------------------------------------------------------')

sex_survive_rate=train.groupby(by='Sex')['Survived'].value_counts()#groupby函数()继续分组
plt.pie(sex_survive_rate.loc['female'],autopct='%.2f%%',labels=['生存','死亡'],pctdistance=0.3,labeldistance=0.75,
        textprops=dict(size=15),colors=['#9400D3','#FFB6C1'])
plt.title('女性生存率')
plt.savefig("sex_survive_rate.png")
#plt .show()

plt.pie(sex_survive_rate.loc['male'],autopct='%.2f%%',labels=['死亡','生存'],pctdistance=0.5,labeldistance=0.75,
        textprops=dict(size=15),colors=['#2E8B57','#AFEEEE'])
plt.title('男性生存率')
plt.savefig("sex_survive_rate1.png")
#plt .show()


embark_survive_rate=train.groupby(by='Embarked')['Survived'].value_counts()
print(embark_survive_rate)
plt.pie(embark_survive_rate.loc['Q'],autopct='%.3f%%',labels=['生存','死亡'],colors=['red','blue'],labeldistance=0.85,textprops={'size':15})
plt.title('Q港口生存率')
plt.savefig("QQQembark_survive_rate1.png",dpi=600)
#plt.show()
plt.pie(embark_survive_rate.loc['C'],autopct='%.3f%%',labels=['死亡','生存'],colors=['red','blue'],labeldistance=0.85,textprops={'size':15})
plt.title('C港口生存率')
plt.savefig("CCCembark_survive_rate1.png",dpi=600)
#plt.show()
plt.pie(embark_survive_rate.loc['S'],autopct='%.3f%%',labels=['生存','死亡'],colors=['red','blue'],labeldistance=0.85,textprops={'size':15})
plt.title('S港口生存率')
plt.savefig("SSSembark_survive_rate1.png",dpi=600)
#plt.show()
print('--------------------------------------------------------------------------------------------------------')

age_range = train['Age']
#统计每个年龄段总人数
age_num,age_num_bins = np.histogram(age_range,range=[0,80],bins=16 )  #统计,对数据进行遍历,range[]对应最小最大值,bins为区间个数,对处于区间内的数据计数,返回一个数组
#histogram函数返回两个数组,要用两个数组接受,第一个数组是,每个区间的的数据,第二个数组是bins区间,也就是0,5,10,15...
print(age_num)
age_survived=[]
for x in range(5,81,5):      #统计每一个年龄区间存活的人数
    survived_num = train.loc[(age_range>=x-5) & (age_range<=x)]['Survived'].sum()
    age_survived.append(survived_num)
plt.figure(figsize=(12,6))#创建宽12,高6的图
plt.bar(np.arange(2,78,5)+0.5,age_num,width=5,label='总人数',alpha=0.8)  #bar()函数画直方图,参数分别为:x轴范围分布(要与数组对应,不然报错),数据,柱宽,标签
plt.bar(np.arange(2,78,5)+0.5,age_survived,width=5,label='生还人数')      #受到width影响,柱状图不对齐0刻度,所以+2.5进行微调
plt.xticks(range(0,81,5)) #x轴上的刻度标志
plt.yticks(range(0,121,10))#y轴刻度标准
plt.xlabel('年龄',fontsize=20)#给xy轴加标签,fontsize文字字号
plt.ylabel('人数',fontsize=20)
plt.title('各年龄阶段人数和生还人数条形图')
plt.savefig('age_survived.png',dpi=500)
#plt.show()

print('------------------------------------------------------------------------------')
'''统计每种票价的情况'''
fare_condition=train.groupby(by='Fare')['Survived'].value_counts()
fare_condition = pd.DataFrame(fare_condition)#转化为Dateframe二维表格
fare_condition.rename(columns={'Survived':'Number'},inplace=True)#rename函数改变列的名字,column={'源数据列名':'新列名'},inplace=true代表不创建新对象,修改源对象
fare_condition.reset_index(inplace=True)#reset_index() 主要可以将数据表中的索引还原为普通列并重新变为默认的整型索引
'''统计每一种票价的总人数'''
fare_all_num = fare_condition.groupby(by='Fare')['Number'].sum()
fare_all_num = pd.DataFrame(fare_all_num)
fare_all_num.rename(columns={'Number':'Total'})
fare_all_num.reset_index(inplace=True)
fare_all_num.rename(columns={'Number':'Total'},inplace=True)
'''统计每一种票价活下来的人数'''
fare_survived = fare_condition.loc[fare_condition['Survived']==1]
#两个表格合并
fare_survived = fare_survived.merge(fare_all_num,on=['Fare'],how='inner')#它的作用是可以根据一个或多个键将不同的DatFrame链接起来,on=共同的键

#计算每一种票价的生还率
survived_rate = fare_survived['Number'].div(fare_survived['Total'])#div除法函数
survived_rate.index = fare_survived['Fare']#改变索引
plt.figure(figsize=(2*10,5))

# 乘客的生还率和票价关系散点图
axes1=plt.subplot(1,2,1)
axes1.scatter(survived_rate.index,survived_rate,marker='o',color='r')
axes1.set_title('乘客生还率和票价关系散点图')
plt.savefig("fare_survive_rate.png",dpi=1000)
plt.show()