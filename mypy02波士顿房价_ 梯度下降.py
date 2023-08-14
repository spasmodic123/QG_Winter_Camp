# encoding = utf-8
import numpy as np
import matplotlib.pyplot as plt


def load_file():
    boston = np.fromfile("housing.data", sep=' ')  # 读进来的是一个一维数组
    feature_name = ["CRIN", "ZN", "INDUS", "CHAX", "NOX", "RM", "AGE", "DIS", "RAD",
                    "TAX", "PIRATIO", "B", "LSTAT", "MEDV"]
    feature_num = len(feature_name)

    # 划分行列,行向量为样本,列向量为特征 的 二维数组
    boston = boston.reshape([boston.shape[0] // feature_num, feature_num])

    # 划分训练集和测试集
    rate = 0.8
    offset = int(boston.shape[0] * rate)
    train_data = boston[:offset]
    test_data = boston[offset:]

    # 数据预处理, 数据归一化,原始数据经过数据归一化/标准化处理后，各指标处于同一数量级
    maximum = train_data.max(axis=0)  # axis=0代表竖轴,从左往右求每一列最大最小
    minimum = train_data.min(axis=0)
    average = train_data.sum(axis=0) / train_data.shape[0]

    global max
    global min
    global avg
    max = maximum
    min = minimum
    avg = average

    # 归一化处理开始,归一化公式
    for i in range(feature_num):
        boston[:, i] = (boston[:, i] - min[i]) / (max[i] - min[i])

    train_data = boston[:offset]
    test_data = boston[offset:]

    return train_data, test_data


class Gradient_descent_method():
    def __init__(self):
        # 随机生存权重w的值
        self.w = np.random.randn(13, 1)  # 生成14行1列的数组,对应权重
        self.b = 0.

    # 预测函数
    def predict(self, x):  # x参数为样本矩阵
        z = np.dot(x, self.w) + self.b
        return z

    # 损失函数
    def lost(self, z, y):  # z参数为预测值,y参数为真实值
        error = y - z
        sample_num = error.shape[0]  # 对于二维数组,shape[0]行,shape[1]列;一维度数组shape[0]表示个数
        fangcha = np.sum(error ** 2) / sample_num  # 损失函数公式
        return fangcha

    # 求梯度,根据偏导公式
    def gradient(self, x, y):
        z = self.predict(x)
        sample_num = x.shape[0]
        gra_w = 1.0 / sample_num * np.sum((z - y) * x,axis=0) # 返回的梯度必须也是每一列分别计算,对应每一列的梯度,所以需要加axis=0
        gra_b = 1.0 / sample_num * np.sum(z - y)
        gra_w = gra_w[:,np.newaxis]  # 将上面的一维数组gra_w升为二维,也就是列向量形式,才可以用于后续的计算
        #print(gra_w)
        return gra_w, gra_b

    # 更新权重
    def update(self, gra_w, gra_b, eta):  # eta为学习率
        self.w = self.w - eta * gra_w
        self.b = self.b - eta * gra_b


    # 训练函数
    def train(self, train_data, num_of_epochs, batch_size, eta):
        n = len(train_data)
        losses = []
        """数据太多,为提高效率,将数据分为5个包--epoch,再分为多个batch,
        每个batch的大小为10"""
        for epoch_id in range(num_of_epochs):
            # 每一轮迭代开始之前,打乱数据,然后按batch_size大小取出小包
            np.random.shuffle(train_data)
            mini_batchs = [train_data[i:i + batch_size] for i in range(0, n, batch_size)]
            for inter_id, mini_batch in enumerate(mini_batchs):
                x = mini_batch[:, :-1]  # -1代表最后一列,包头不包尾
                y = mini_batch[:, -1:]
                z = self.predict(x)
                loss = self.lost(z, y)
                gra_w, gra_b = self.gradient(x, y)
                self.update(gra_w, gra_b, eta)
                losses.append(loss)
                #print("epoch:  {0}\ninter:{1}\nloss:{2}".format(epoch_id,inter_id,loss))
        # 测试数据
        self.load_one_example(test_data)
        return losses

    # 预测程序

    def load_one_example(self,test_data):
        idx = 6  # 随机选取一行测试
        one_data, label = test_data[idx, :-1], test_data[idx, -1]
        z = np.dot(one_data,self.w ) + self.b
        print("预测集的误差为\n",z-label)


# 获取数据
train_data, test_data = load_file()

# 训练开始
a = Gradient_descent_method()
lossess = a.train(train_data,num_of_epochs=20,batch_size=100, eta=0.1)

# 绘图
plot_x = np.arange(len(lossess))
plot_y = np.array(lossess)
plt.plot(plot_x,plot_y)
plt.savefig("损失函数图像",dpi=999)
plt.show()


