import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# generate random data
np.random.seed(0)
X = np.random.rand(100, 1)
y = 2 + 3 * X + np.random.rand(100, 1)

# fit the model to the data
reg = LinearRegression().fit(X, y)

# make predictions
y_pred = reg.predict(X)

# plot the original data and the prediction line
plt.scatter(X, y)
plt.plot(X, y_pred, color='red')
plt.show()
