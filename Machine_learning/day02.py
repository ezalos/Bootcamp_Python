import math

def sigmoid_(x, L=1, k=1, x0=0):
	"""
	Compute the sigmoid of a scalar or a list.
	Args:
		x: a scalar or list
	Returns:
		The sigmoid value as a scalar or list.
		None on any error.
	Raises:
		This function should not raise any Exception.
	"""
	if isinstance(x, type([])):
		answer = []
		for i in range(len(x)):
			e = math.exp(-k * (x[i] - x0))
			top = L
			bot = 1 + e
			answer.append(top / bot)
	else:
		e = math.exp(-k * (x - x0))
		top = L
		bot = 1 + e
		answer = (top / bot)
	return answer


x = -4
print(sigmoid_(x))
# 0.01798620996209156
x = 2
print(sigmoid_(x))
# 0.8807970779778823
x = [-4, 2, 0]
print(sigmoid_(x))
# [0.01798620996209156, 0.8807970779778823, 0.5]


def log_loss_(y_true, y_pred, m, eps=1e-15):
	"""
	Compute the logistic loss value.
	Args:
		y_true: a scalar or a list for the correct labels
		y_pred: a scalar or a list for the predicted labels
		m: the length of y_true (should also be the length of y_pred)
		eps: epsilon (default=1e-15)
	Returns:
		The logistic loss value as a float.
		None on any error.
	Raises:
		This function should not raise any Exception.

		-(1/m) * Sum(y * )
	"""
	print(y_true.shape)
	print(y_pred.shape)
	for elem in y_true:

	return answer

# Test n.1
x = 4
y_true = 1
theta = 0.5
y_pred = sigmoid_(x * theta)
m = 1 # length of y_true is 1
print(log_loss_(y_true, y_pred, m))
# 0.12692801104297152

# Test n.2
x = [1, 2, 3, 4]
y_true = 0
theta = [-1.5, 2.3, 1.4, 0.7]
x_dot_theta = sum([a*b for a, b in zip(x, theta)])
y_pred = sigmoid_(x_dot_theta)
m = 1
print(log_loss_(y_true, y_pred, m))
# 10.100041078687479

# Test n.3
x_new = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
y_true = [1, 0, 1]
theta = [-1.5, 2.3, 1.4, 0.7]
x_dot_theta = []
for i in range(len(x_new)):
 my_sum = 0
 for j in range(len(x_new[i])):
 my_sum += x_new[i][j] * theta[j]
 x_dot_theta.append(my_sum)
y_pred = sigmoid_(x_dot_theta)
m = len(y_true)
print(log_loss_(y_true, y_pred, m))
# 7.233346147374828
