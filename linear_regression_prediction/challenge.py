import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np

#read data
dataframe = pd.read_csv('challenge_dataset.txt', sep=",", header=None, names=["x", "y"])
x_values = dataframe[['x']]
y_values = dataframe[['y']]

#train model
body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)

# The coefficients
print('Coefficients: ', body_reg.coef_)
# The mean squared error
print('Mean squared error: %.2f ' % np.mean((body_reg.predict(x_values) - y_values) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % body_reg.score(x_values, y_values))

#Visualize Results
plt.scatter(x_values, y_values)
plt.plot(x_values, body_reg.predict(x_values))
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Challenge Dataset')
plt.show()
