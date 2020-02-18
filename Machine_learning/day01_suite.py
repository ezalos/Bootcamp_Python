import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from mylinearregression import MyLinearRegression as MyLR
import matplotlib.pyplot as plt

path = "ressources/day01/resources/"
data = pd.read_csv(path + "are_blue_pills_magics.csv")
Xpill = np.array(data["Micrograms"]).reshape(-1,1)
Yscore = np.array(data["Score"]).reshape(-1,1)

linear_model1 = MyLR(np.array([[89.0], [-8]]))
linear_model2 = MyLR(np.array([[89.0], [-6]]))
Y_model1 = linear_model1.predict_(Xpill)
Y_model2 = linear_model2.predict_(Xpill)

# print("NB1", linear_model1.mse_(Y_model1, Yscore))
print("NB1", linear_model1.mse_(Xpill, Yscore))
# 57.60304285714282
print("NB2", mean_squared_error(Yscore, Y_model1))
# 57.603042857142825
# print("NB1", linear_model2.mse_(Y_model2, Yscore))
print("NB3", linear_model2.mse_(Xpill, Yscore))
# 232.16344285714285
print("NB4", mean_squared_error(Yscore, Y_model2))
# 232.16344285714285


data.plot.scatter("Micrograms", "Score")
# plt.show()

x = np.linspace(0,10,100)
y = linear_model1.theta[0] + (linear_model1.theta[1] * x)
plt.plot(x, y, '-r', label='Linear model 1')
# plt.title('Linear model 1')
y = linear_model2.theta[0] + (linear_model2.theta[1] * x)
plt.plot(x, y, '-r', label='Linear model 2', color = "blue")

linear_model2.fit_(Xpill, Yscore, alpha = 1.6e-4, n_cycle=200000)

y = linear_model2.theta[0] + (linear_model2.theta[1] * x)
plt.plot(x, y, '-r', label='Linear model 2', color = "green")
plt.legend(loc='lower left')
plt.grid()
plt.show()






# theta = np.linspace(-14,-4,5)
# print(theta)
# print(x)
# for i in range(theta.shape[0]):
# 	sol = []
# 	for j in range(x.shape[0]):
# 		elem = MyLR(np.array([[theta[i]], [x[j]]]))
# 		sol.append( elem.mse_(Xpill, Yscore))
# 		print(elem.theta, sol)
# 		# print(linear_model1.theta)
# 	plt.plot(theta[i], sol, label='Theta exp')
# plt.grid()
# plt.show()
