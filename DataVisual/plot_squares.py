# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

'''
#绘制折线图 使用函数plot()
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)
plt.title("折线图", fontsize=24)   #设置图表标题，并给坐标轴加上标签
plt.xlabel("value", fontsize=14)    #设置x轴标题
plt.ylabel("squares of value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)  #设置刻度标记的大小，axis=both实参将影响X和Y轴
plt.show()
'''

'''
#绘制散点图 使用函数scatter()
#x = [1, 2, 3, 4, 5]
#y = [1, 4, 9, 16, 25]
x = list(range(1, 1001))
y = list(i**2 for i in x)
plt.scatter(x, y, s=20) #s=20,设置点的大小
plt.title("散点图", fontsize=24)    #设置图表标题，并给坐标轴加上标签
plt.xlabel("value", fontsize=14)    #设置x轴标题
plt.ylabel("squares of value", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)  #设置刻度标记的大小，axis=both实参将影响X和Y轴
plt.show()
'''

#模拟随机漫步
from random import choice
import time
class RandomWalk():
    '''一个生成随机漫步数据的类'''
    def __init__(self, num_points=1000):
        '''初始化随机漫步函数'''
        self.num_points = num_points
        self.x_values = [0] #所有随机漫步都始于0
        self.y_values = [0]

    def fill_walk(self):
        '''计算随机漫步包含的所有点'''
        while len(self.x_values) < self.num_points: #不断漫步， 直到列表达到指定的长度
            x_direction = choice([1, -1])   #决定前进方向及沿这个方向前进的距离
            x_distance = choice([0, 1, 2, 3, 4])
            x_steps = x_direction * x_distance
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_steps = y_direction * y_distance
            if x_steps == 0 and y_steps == 0:
                continue
            next_x = self.x_values[-1] + x_steps
            next_y = self.y_values[-1] + y_steps
            self.x_values.append(next_x)
            self.y_values.append(next_y)
rw = RandomWalk()
rw.fill_walk()
plt.title(u"RandomWalk", fontsize=24)
plt.scatter(rw.x_values, rw.y_values, s=15)
print("随机漫步图")
plt.show()
