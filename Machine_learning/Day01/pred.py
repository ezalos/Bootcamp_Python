import numpy as np

def predict_(theta, X):
	"""
	Description:
		Prediction of output using the hypothesis function (linear model).
	Args:
		theta: has to be a numpy.ndarray, a vector of dimension (number of
		features + 1, 1).
		X: has to be a numpy.ndarray, a matrix of dimension (number of
		training examples, number of features).
	Returns:
		pred: numpy.ndarray, a vector of dimension (number of the training
		examples,1).
		None if X does not match the dimension of theta.
	Raises:
		This function should not raise any Exception.
	"""
	print("Shape X : ", X.shape)
	print("Shape Th : ", theta.shape)
	m = X.shape[0] #nb_features
	n = X.shape[1] #nb_training_examples
	nb_features = theta.shape[0] - 1
	if n != nb_features or (len(theta.shape) > 1 and theta.shape[1] != 1):
		print("Incompatible dimension match between X and theta.")
		return None
	answer = []
	for i in range(n):
		answer.append(theta @ X[i])
	pred = np.array(answer)
	print(pred)
	return pred

X1 = np.array([[0.], [1.], [2.], [3.], [4.]])
theta1 = np.array([[2.], [4.]])
predict_(theta1, X1)
# array([[2], [6], [10], [14.], [18.]])
X2 = np.array([[1], [2], [3], [5], [8]])
theta2 = np.array([[2.]])
predict_(theta2, X2)
# Incompatible dimension match between X and theta.
# None
X3 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8.,
80.]])
theta3 = np.array([[0.05], [1.], [1.], [1.]])
predict_(theta3, X3)
# array([[22.25], [44.45], [66.65], [88.85]])
