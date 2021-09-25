import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mean,sigma=8,1.5

# input feature 1 using normal distribution
x1 = abs(np.random.normal(mean, sigma, 20))

# input feature 2 using normal distribution
x2 = abs(np.random.normal(mean, sigma, 20))

x = np.c_[x1, x2]
y = [np.random.binomial(100, 0.6, 20)]

data_set = pd.DataFrame()

# defining the columns of the dataset
data_set['col1'] = x1
data_set['col2'] = x2

# 2D Projection of Dataset
plt.subplot(121)
plt.title('X1 Input Feature VS Y Output Feature', fontsize='small')
plt.scatter(y, x1, color='r', label='col1')
plt.xlabel('y')
plt.ylabel('x1')

plt.subplot(122)
plt.title('X2 Input Feature VS Y Output Feature', fontsize='small')
plt.scatter(y, x2, color='b', label='col2')
plt.xlabel('y')
plt.ylabel('x2')


# 3D Projection of Dataset
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(x1, x2, y, c=y, cmap='hot_r')
ax.set_title('3D Projection of Dataset')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')

plt.show()