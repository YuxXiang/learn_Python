import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 创建一个随机的二维数组作为示例数据
data = np.random.rand(6, 4)  # 6行4列的矩阵

# 使用seaborn的heatmap函数绘制热力图
sns.heatmap(data, annot=True, fmt=".2f", cmap="coolwarm")

# 显示图表
plt.show()