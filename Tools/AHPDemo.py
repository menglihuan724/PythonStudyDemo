# 思路：
# 1.首先输入每个指标下面对应的判断矩阵，
# 该矩阵中的值是通过大数据（或者专家）得到的每两个指标之间的相对重要程度值，
# 通过AHP计算这些判断矩阵是否通过一致性的检验，通过即合理，
# 不通过就说明矩阵中的两指标间的相对重要程度有过分矛盾的地方，

import numpy as np


# 定义一个叫AHP的类
class AHP:
    def __init__(self, array):  # array是每个指标下面对应的判断矩阵，即原始数据
        self.row = len(array)  # 计算矩阵的行数
        self.col = len(array[0])  # 计算矩阵的列数

    def get_tezheng(self, array):  # 获取最大特征值和对应的特征向量
        te_val, te_vector = np.linalg.eig(array)  # numpy.linalg.eig() 计算矩阵特征值与特征向量
        list1 = list(te_val)  # te_val是一个一行三列的矩阵，此处将矩阵转化为列表
        print("特征值为：", te_val)
        print("特征向量为：", te_vector)

        # 得到最大特征值对应的特征向量
        max_val = np.max(list1)  # 最大特征值
        index = list1.index(max_val)  # 最大特征值在列表中的位置
        max_vector = te_vector[:, index]  # 通过位置来确定最大特征值对应的特征向量
        print(f'最大的特征值:" + {max_val} + "   对应的特征向量为：" + {max_vector}')
        return max_val, max_vector

    def RImatrix(self, n):  # 建立RI矩阵，该矩阵是AHP中自带的，类似标杆一样，除n之外的值不能更改
        d = {}
        n1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        n2 = [0, 0, 0.58, 0.90, 1.12, 1.24, 1.32, 1.41, 1.45]
        for i in range(n):  # 获取n阶矩阵对应的RI值
            d[n1[n]] = n2[n]
        print("该矩阵在一致性检测时采用的RI值为：", d[n1[n]])
        return d[n1[n]]

    def test_consitstence(self, max_val, RI):  # 测试一致性，AHP中最重要的一步，用于检验判断矩阵中的数据是否自相矛盾
        CI = (max_val - self.row) / (self.row - 1)  # AHP中计算CI的标准公式
        CR = CI / RI  # AHP中计算CR的标准公式
        if CR < 0.10:
            print(f'判断矩阵的CR值为  " + {CR} + "通过一致性检验"')
            return True
        else:
            print(f'"判断矩阵的CR值为  " + {CR} + "判断矩阵未通过一致性检验，请重新输入判断矩阵"')
            return False

    def normalize_vector(self, max_vector):  # 特征向量归一化
        vector_after_normalization = []  # 生成一个空白列表，用于存放归一化之后的特征向量的值
        sum0 = np.sum(max_vector)  # 将特征向量的每一个元素相加取和
        for i in range(len(max_vector)):
            # 将特征向量的每一个元素除以和，得到比值，保证向量的每一个元素都在0和1之间，直线归一化
            # 将归一化之后的元素依次插入空白列表的尾部
            vector_after_normalization.append(max_vector[i] / sum0)
        print(f'"该级指标的权重矩阵为：  " + {vector_after_normalization}')
        return vector_after_normalization

    def weightCalculator(self, normalMatrix):  # 计算最终指标对应的权重值
        # layers weight calculations.
        listlen = len(normalMatrix) - 1  # 设置listlen的初始值为normalMatrix最后一个元素的index
        layerWeights = list()  # 空白权重列表
        while listlen > -1:
            sum = float()  # sum的初始值为0.0，并且限制了sum的类型为浮点型
            for i in normalMatrix:
                sum += i[listlen]  # 求normalMatrix各元素的和
            sumAverage = round(sum / len(normalMatrix), 3)  # 求normalMatrix各元素的平均值，并保留三位小数
            layerWeights.append(sumAverage)  # 为什么平均值是权重？？？？？？
            listlen -= 1
        return layerWeights




 # 这里需要确定指标的规模即多少个一级指标，多少个二级指标，这样才能确定要计算多少个对比矩阵
def define_structure():  # 构造AHP的层次结构
    level_structure = []
    level = int(input("请输入指标的级数："))  # 输入比如说这是个三级指标体系
    # level0 = input("请输入每一级下指标的个数：")
    # level_structure.append(level0)  # 将列表level0作为一个元素插入到列表level的末尾
    level2 = []
    for i in range(level):  # 每一级指标下有多少具体的指标个数
        rate_num =int( input(f'请输入" + {i} + "层下指标的个数：'))
        # level2.append(rate_num)
        for j in range(rate_num):
            two_level_for_one = int(input(f'请输入第" + {j} + " 个一级指标对应的下级指标的个数：'))
            level_structure.append(two_level_for_one)
    return level_structure


def creat_matrix(n):
    array1 = []
    array2 = []
    n = define_structure()
    for i in n:
        length = input("请输入指标对比矩阵的阶数：")  # 对应指标下共有多少个相互对比的对象
        length = int(length)  # 向下取整，若length=3.7，则int(length)=3
        count = 0
    for i in range(length):  # 若length=3，则这部分实现的是，输入矩阵中3*3=9个元素的值
        for j in range(length):
            count += 1
            x = input(f'请输入指标对比矩阵的第" + {count} + " 个元素：')
            x = float(x)
            array1.append(x)  # 此时的array1还不是一个矩阵，只是包含9个元素的列表
        # eg:array1=[4,7,8,2,1,13,16,5,11]
    for i in range(length * length):  # 将列表array1矩阵化
        if (i + 1) % length == 0:  # 使用i+1是为了避免i=0的情况，因为0%3==0是true
            array2.append(array1[i - length + 1:i + 1])  # 每3个元素形成一个列表插入到array2的末尾
    print(array2)  # eg：array2=[[4,7,8],[2,1,13],[16,5,11]]矩阵形式

    array2 = np.mat(array2)  # NumPy函数库中的matrix与MATLAB中matrices等价，由于AHP是比较数学的东西，所以习惯的mat一下矩阵
    a = AHP(array2)
    max_val, max_vector = a.get_tezheng(array2)  # 获取最大特征值和对应的特征向量
    RI = a.RImatrix(length)  # 获取length阶矩阵对应的RI值
    flag = a.test_consitstence(max_val, RI)  # 测试一致性，返回TRUE或者flase
    if flag:  # 如果flag=TRUE，则调用函数通过最大特征值对应的特征向量获取权重矩阵
        weight = a.normalize_vector(max_vector)

if __name__ == "__main__":
    creat_matrix(3)
