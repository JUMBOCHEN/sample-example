import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)
plt.title("squares numbers", fontsize=24)   #设置图表标题，并给坐标轴加上标签

plt.xlabel("value", fontsize=14)    #设置x轴标题
plt.ylabel("squares of value", fontsize=14)

plt.tick_params(axis='both', labelsize=14)  #设置刻度标记的大小，axis=both实参将影响X和Y轴

plt.show()