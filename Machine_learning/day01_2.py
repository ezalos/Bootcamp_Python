import pandas as pd
import numpy as np
from mylinearregression import MyLinearRegression as MyLR
import matplotlib.pyplot as plt

path = "ressources/day01/resources/"
data = pd.read_csv(path + "spacecraft_data.csv")
X = np.array(data[['Age','Thrust_power','Terameters']])
Y = np.array(data[['Sell_price']])
my_lreg = MyLR([1.0, 1.0, 1.0, 1.0])
my_lreg.theta = my_lreg.theta.reshape(-1,1)
print(X.shape)
print(Y.shape)
print(my_lreg.theta.shape)
print(my_lreg.mse_(X,Y))

data.plot.scatter("Thrust_power", "Sell_price")
x = np.linspace(0,200,100)
y = my_lreg.theta[0] + (my_lreg.theta[2] * X[2])
# plt.plot(X[2], y, '-r', label='Linear model 1', color = "green")
plt.plot(x, my_lreg.theta[0] + (my_lreg.theta[2] * x), '-r', label='Linear model 1', color = "red")

plt.legend(loc='upper left')
plt.grid()
plt.show(block=False)


# 144044.877...
my_lreg.fit_(X,Y, alpha = 5e-5, n_cycle = 60000)
print(my_lreg.theta)
# array([[334.994...],[-22.535...],[5.857...],[-2.586...]])
print(my_lreg.mse_(X,Y))
# 586.896999...

# plt.show()

x = np.linspace(0,200,100)
y = my_lreg.theta[0] + (my_lreg.theta[2] * X[2])
# plt.plot(X[2], y, '-r', label='Linear model 1', color = "yellow")
plt.plot(x, my_lreg.theta[0] + (my_lreg.theta[2] * x), '-r', label='Linear model 1', color = "yellow")
# plt.title('Linear model 1')
# plt.plot(X[2], Y, '-r', label='Linear model 2', color = "blue")

plt.legend(loc='upper left')
plt.grid()
plt.show()
