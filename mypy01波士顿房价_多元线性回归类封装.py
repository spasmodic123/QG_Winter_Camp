import numpy as np
import pandas as pd


class multiLinerRegression:
    def __init__(self, filename):
        self.weight = None  # 权重
        self.load_file(filename)
        self.train(self.train_x, self.train_y)  # 训练集
        self.predict(self.predict_x)  # 测试集
        self.mistake(self.real_y,self.predict_result)

    def load_file(self, filename):
        # 从文件中导入数据
        boston = pd.read_csv(filename)
        boston = boston.dropna()  # 删除有空元素的行

        # 划分训练集和测试机,比例为80% 20%
        offset = int(boston.shape[0] * 0.8)
        train_data = boston[:offset]
        predict_data = boston[offset:]

        self.train_x = train_data.loc[0:, "CRIM":"LSTAT"]  # 将特征和标签分开
        self.train_y = train_data.loc[0:, "MEDV"]
        self.predict_x = predict_data.loc[0:, "CRIM":"LSTAT"]
        self.real_y = predict_data.loc[0:, "MEDV"]

    def train(self, train_x, train_y):
        assert (train_x.shape[0] == train_y.shape[0])  # 确保有几个样本,就有多少个y
        one = np.ones((train_x.shape[0], 1))  # 全部是1,作为欧米噶0,也就是b偏移量
        character = np.hstack((one, train_x))  # 合并,形成特征值的矩阵,也就是变量
        character = np.mat(character)  # 转化为矩阵,一定要注意哪一个原本是行向量,哪一个原本是列向量
        train_y = np.mat(train_y).T
        self.weight = np.linalg.inv(character.T.dot(character)).dot(character.T).dot(train_y)  # 根据权重公式,w= (X^T *
        # X)^{-1} * X^T * y
        print("计算的权重向量为:\n", self.weight)
        print('----------------------------------\n\n')
        return self

    def predict(self, predict_x):
        one = np.ones((predict_x.shape[0], 1))
        character = np.hstack((one, predict_x))
        character = np.mat(character)  # 转化为矩阵,一定要注意哪一个原本是行向量,哪一个原本是列向量
        self.predict_result = character.dot(self.weight)
        print("预测结果为:\n", self.predict_result)
        print('----------------------------------\n\n')


    def mistake(self, real_y, predict_y):
        loss = 0
        real_y = np.array(real_y)   #从Series转化为数组
        lenght=len(real_y)-1
        for i in range(lenght-1):
            loss += (real_y[i]-predict_y[i,0])**2     # 最小二乘法计算误差
        loss = loss/len(real_y)
        print("损失函数的值为:",loss )


a = multiLinerRegression(r"boston_housing_data.csv")
