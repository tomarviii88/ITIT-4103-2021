import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Label 0
# 1st Input Feature
x11 = abs(np.random.normal(8, 1.5, 20))
# 2nd Input Feature
x12 = abs(np.random.normal(8, 1.5, 20))
x1 = np.c_[x11, x12]
y1 = [np.random.binomial(10, 0.6, 20)]


# Dataframe to save dataset
data = pd.DataFrame()
data['input1'] = x11
data['input2'] = x12

# Plot of input features with Label 0 vs output features
plt.subplot(221)
plt.title('Label0-Input 1 vs Label')
plt.scatter(y1, x11, color='g', label='col1')
plt.xlabel('y')
plt.ylabel('x1')

plt.subplot(222)
plt.title('Label1-Input 2 vs Label')
plt.scatter(y1, x12, color='b', label='col2')
plt.xlabel('y')
plt.ylabel('x2')
plt.show()

fig = plt.figure()

ax = plt.axes(projection='3d')
ax.scatter3D(x11, x12, y1, c=y1, cmap='hot_r')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')
plt.show()


# Label-1
# 1st Input Feature
x21 = abs(np.random.normal(15, 1.5, 20))
# 2nd Input Feature
x22 = abs(np.random.normal(15, 1.5, 20))
x2 = np.c_[x21, x22]
y2 = [np.random.binomial(10, 0.6, 20)]

# Dataframe to save the data
data = pd.DataFrame()
data['input1'] = x21
data['input2'] = x22

# Plot of input features with Label 0 vs output features
plt.subplot(221)
plt.title('Label1-Input 1 vs Label')
plt.scatter(y2, x21, color='g', label='col1')
plt.xlabel('y')
plt.ylabel('x1')

plt.subplot(222)
plt.title('Label1-Input 1 vs Label')
plt.scatter(y2, x22, color='b', label='col2')
plt.xlabel('y')
plt.ylabel('x2')
plt.show()

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter3D(x21, x22, y2, c=y2, cmap='hot_r')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')

plt.show()