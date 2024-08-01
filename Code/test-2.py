
# 以下是使用TensorFlow实现的简单神经网络回归模型示例，
# 使用加利福尼亚房价数据集（California housing dataset）进行建模和预测：
# 
# pip3 install tensorflow scikit-learn numpy matplotlib


"""
This script demonstrates a simple neural network regression model using TensorFlow.
It uses the California housing dataset for modeling and prediction.

Requirements:
- pip3 install tensorflow scikit-learn numpy matplotlib

Steps:
1. Load the California housing dataset.
2. Preprocess the data by standardizing the features.
3. Split the dataset into training and testing sets.
4. Build a neural network model with two hidden layers and a linear output layer.
5. Compile the model with the Adam optimizer and mean squared error loss.
6. Train the model on the training set.
7. Evaluate the model on the testing set.
8. Plot the training and validation loss curves.
9. Use the trained model to make predictions on the testing set.
10. Plot the predicted values against the true values.

"""

import tensorflow as tf
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

# 加载加利福尼亚房价数据集
housing = fetch_california_housing()

# 提取特征和目标变量
X, y = housing.data, housing.target

# 数据预处理：标准化特征
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 划分数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 构建神经网络模型
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)  # 线性输出层，用于回归预测
])

# 编译模型
model.compile(optimizer='adam', loss='mean_squared_error')

# 训练模型
history = model.fit(X_train, y_train, epochs=100, validation_split=0.2, verbose=0)

# 评估模型
mse_test = model.evaluate(X_test, y_test, verbose=0)
print(f'Mean Squared Error on Test Set: {mse_test:.2f}')

# 绘制训练过程中的损失曲线
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# 使用模型进行预测
y_pred = model.predict(X_test)

# 绘制预测结果与真实结果的对比图
plt.scatter(y_test, y_pred)
plt.xlabel('True Values')
plt.ylabel('Predictions')
plt.title('True Values vs Predictions')
plt.show()
