import random
import numpy as np
import pandas as pd

# 载入数据
def load_file(file_name):
    featrue_num = 5
    data = pd.read_csv(file_name)
    data = data.loc[0:, "Sepal.Length":"Species"]
    data_sample = data.loc[0:, "Sepal.Length":"Petal.Width"]
    data_label = data.loc[0:, "Species"]
    data_sample = np.array(data_sample)
    #print(data_sample)
    return data_sample,data_label


class K_means():
    def __init__(self):
        self.leight = data_sample.shape[0]  # 样本数量
        self.featrue_num = data_sample.shape[1]  # 特征数量

    # 随机生成4个样本中心的位置
    def creat_center(self):  # 有四个特征,所以维度为4,每一个点对应为(a,b,c,d)
        self.a1 = random.randint(1, 10); self.a2 = random.randint(1, 10);self.a3 = random.randint(1, 10);self.a4=random.randint(1, 10)
        self.b1 = random.randint(1, 10); self.b2 = random.randint(1, 10);self.b3 = random.randint(1, 10);self.b4=random.randint(1, 10)
        self.c1 = random.randint(1, 10); self.c2 = random.randint(1, 10);self.c3 = random.randint(1, 10);self.c4=random.randint(1, 10)
        self.d1 = random.randint(1, 10); self.d2 = random.randint(1, 10);self.d3 = random.randint(1, 10);self.d4=random.randint(1, 10)

        # 定义两点间的距离
    def distance(self, data_sample):  # a,b,c,d分别是四个维度,对应四个特征
        # 计算每个样本到四个随机中心点的距离
        self.center_distance01 = [np.sqrt( (data_sample[i][0]-self.a1)**2 + (data_sample[i][1]-self.b1)**2 + (data_sample[i][2]-self.c1)**2 + (data_sample[i][3]-self.d1)**2 ) for i in range(self.leight)]
        self.center_distance02 = [np.sqrt( (data_sample[i][0]-self.a2)**2 + (data_sample[i][1]-self.b2)**2 + (data_sample[i][2]-self.c2)**2 + (data_sample[i][3]-self.d2)**2 ) for i in range(self.leight)]
        self.center_distance03 = [np.sqrt( (data_sample[i][0]-self.a3)**2 + (data_sample[i][1]-self.b3)**2 + (data_sample[i][2]-self.c3)**2 + (data_sample[i][3]-self.d3)**2 ) for i in range(self.leight)]
        self.center_distance04 = [np.sqrt( (data_sample[i][0]-self.a4)**2 + (data_sample[i][1]-self.b4)**2 + (data_sample[i][2]-self.c4)**2 + (data_sample[i][3]-self.d4)**2 ) for i in range(self.leight)]

        # 将距离最近的中心点,作为自己所在的蔟(类)
    def find_nearext(self,data_sample):
        self.cluster01 = []
        self.cluster02 = []
        self.cluster03 = []
        self.cluster04 = []
        # 把每一个样本点归类于距离最近的中心点(蔟)
        for i in range(self.leight):
            tmp = min(self.center_distance01[i],self.center_distance02[i],self.center_distance03[i],self.center_distance04[i])
            if tmp == self.center_distance01[i]:
                self.cluster01.append(data_sample[i])
            elif(tmp == self.center_distance02[i]):
                self.cluster02.append(data_sample[i])
            elif(tmp == self.center_distance03[i]):
                self.cluster03.append(data_sample[i])
            elif(tmp == self.center_distance04[i]):
                self.cluster04.append(data_sample[i])

    # 更新中心点的位置
    def updata_center(self):
        # 对于不同的蔟,更新不同的中心点
        tmp01,tmp02,tmp03,tmp04 = 0,0,0,0
        # 分别求出每一个特征的坐标的总和,在求平均
        if len(self.cluster01) != 0:
            for i in range(len(self.cluster01)):
                tmp01 += self.cluster01[i][0] ; tmp02 += self.cluster01[i][1]; tmp03 += self.cluster01[i][2]; tmp04 += self.cluster01[i][3]
            self.a1 = tmp01/len(self.cluster01)
            self.b1 = tmp02/len(self.cluster01)
            self.c1 = tmp03 / len(self.cluster01)
            self.d1 = tmp04 / len(self.cluster01)

        tmp01, tmp02, tmp03, tmp04 = 0, 0, 0, 0  # 更新tmp的值,继续计算下一个蔟的坐标平均值
        if len(self.cluster02) != 0:
            for i in range(len(self.cluster02)):
                tmp01 += self.cluster02[i][0] ; tmp02 += self.cluster02[i][1]; tmp03 += self.cluster02[i][2]; tmp04 += self.cluster02[i][3]
            self.a2 = tmp01 / len(self.cluster02)
            self.b2 = tmp02 / len(self.cluster02)
            self.c2 = tmp03 / len(self.cluster02)
            self.d2 = tmp04 / len(self.cluster02)

        tmp01, tmp02, tmp03, tmp04 = 0, 0, 0, 0
        if len(self.cluster03) != 0:
            for i in range(len(self.cluster03)):
                tmp01 += self.cluster03[i][0] ; tmp02 += self.cluster03[i][1]; tmp03 += self.cluster03[i][2]; tmp04 += self.cluster03[i][3]
            self.a3 = tmp01 / len(self.cluster03)
            self.b3 = tmp02 / len(self.cluster03)
            self.c3 = tmp03 / len(self.cluster03)
            self.d3 = tmp04 / len(self.cluster03)

        tmp01, tmp02, tmp03, tmp04 = 0, 0, 0, 0
        if len(self.cluster04) != 0:
            for i in range(len(self.cluster04)):
                tmp01 += self.cluster04[i][0] ; tmp02 += self.cluster04[i][1]; tmp03 += self.cluster04[i][2]; tmp04 += self.cluster04[i][3]

            self.a4 = tmp01 / len(self.cluster04)
            self.b4 = tmp02 / len(self.cluster04)
            self.c4 = tmp03 / len(self.cluster04)
            self.d4 = tmp04 / len(self.cluster04)

    # 训练函数
    def train(self):
        self.creat_center()
        # 循环更新中心点的坐标,知道收敛,或坐标不在改变就停止
        while True:
            a1,b1,c1,d1 = self.a1,self.b1,self.c1,self.d1
            a2, b2, c2, d2 = self.a2, self.b2, self.c2, self.d2
            a3, b3, c3, d3 = self.a3, self.b3, self.c3, self.d3
            a4, b4, c4, d4 = self.a4, self.b4, self.c4, self.d4
            self.distance(data_sample)
            self.find_nearext(data_sample)
            self.updata_center()
            if a1==self.a1 and b1 == self.b1 and c1 == self.c1 and d1 == self.d1\
                and a2==self.a2 and b2 == self.b2 and c2 == self.c2 and d2 == self.d2\
                and a3==self.a3 and b3 == self.b3 and c3 == self.c3 and d3 == self.d3\
                and a4==self.a4 and b4 == self.b4 and c4 == self.c4 and d4 == self.d4:  # 循环多次后,只要其中一个蔟收敛了,另外三个也才差不多了
                break
        num = 0
        if len(self.cluster01) != 0:
            num += 1
        if len(self.cluster02) != 0:
            num += 1
        if len(self.cluster03) != 0:
            num += 1
        if len(self.cluster04) != 0:
            num += 1
        print("训练完成!\n一共分为了{0}蔟".format(num))




data_sample, data_label = load_file(r"C:\Python_Study\Python_K_means\Iris数据集\iris.csv")
a = K_means()
a.train()

