import pandas as pd
#注意格式,注意用逗号隔开
mydateset={
    'car_name':['Rools_Royce','Ferrari','Porsche'],
    'prize':[999999,888888,777777]
}
test01=pd.DataFrame(mydateset)
print(test01,end='\n\n')     #输出的数据最左边是索引

a=['Guangdong','Shanghai','Hangzhou','Haerbin']
test02=pd.Series(a,index=['w','x','y','z'],name='城市省份')    #Series储存一维数据,可以用index指定索引名字,name添加名字
print(test02)
print(test02['w'],end='\n\n')#通过索引访问数据

#可以使用 key/value 对象，类似字典来创建 Series
mingzi={'first':'zhangjiewei','second':'cenbaisen','third':'shijinhua'}
test03=pd.Series(mingzi,name='名字')   #name参数可省略
print(test03,end='\n\n')

#Dateframe可以看作由多个Series组成的字典,比Series多了一个索引--列标签    Dataframe相当于二维数据
b=[['SUN-YET unniversity',985],['FU-DAN university',985],['SHEN-ZHEN university',211]]
test04=pd.DataFrame(b,columns=['UNIVERSITY','Rank'],dtype=float)   #因为数据中有汉字,强制dtype转换float会弹出警告,不会报错
print(test04,end='\n\n')

c={#利用字典格式创建Dataframe
    'UNIERSITY':['SUN-YET unniversity','FU-DAN university','SHEN-ZHEN university'],
    'Rank':[985,985,211]
}
test05=pd.DataFrame(c)
print(test05,end='\n\n')
print(test05.loc[2])    #通过loc返回指定行的数据,索引方式与Series不同


test06=pd.read_csv(r"C:\Users\changan\Downloads\nba.csv")#数据读取
print(test06,end='\n\n')       #如果要打印完全部的数据,要用print(test06.to_string())
print(test06.head(5),end='\n\n')#输出前5行
print(test06.tail(5),end='\n\n')#输出后5行
print(test06.info(),end='\n\n')#输出表格基本信息


nme = ["Google", "Runoob", "Taobao", "Wiki"]
st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
ag = [90, 40, 80, 98]
c={'name':nme,'site':st,'age':ag}
test07=pd.DataFrame(c)
test07.to_csv("C:\pythonProject1\date2.csv")#数据存储,to_csv()函数储存在csv拓展名文件中



z=pd.read_csv(r"C:\Users\changan\Downloads\property-data.csv",na_values=['na','n/a','NA']) #文件地址前加个r,避免转义字符
#读取数据,na_value=,参数,把后面的元素当作空元素 NaN
print(z.isnull(),end='\n\n')    #isnull()函数判断空字符
print(z['PID'].isnull(),end='\n\n')        #索引返回指定列

new_form1=z.dropna()#dropna()函数去除含有空元素的一整行
print(new_form1,end='\n\n')
#默认情况下，dropna() 方法返回一个新的 DataFrame，不会修改源数据。如果你要修改源数据 DataFrame, 可以使用 inplace = True 参数

new_form2=z.dropna(subset='NUM_BATH')     #subset参数检查某一列,如果有一个元素为空,对应这一行被删除
print(new_form2,end='\n\n')

new_form3=z.fillna('靓仔')       #fillna()函数用输入的东西替换空元素
print(new_form3,end='\n\n')


person = {
  "name": ['Google', 'Runoob' , 'Taobao'],
  "age": [50, 40, 12345]    # 12345 年龄数据是错误的
}
test08=pd.DataFrame(person)
test08.loc[2,'age']=36       #修改数据,对应行标签2的一行,列标签age的一列
print(test08,end='\n\n')
