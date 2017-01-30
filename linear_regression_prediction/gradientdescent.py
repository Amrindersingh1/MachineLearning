from numpy import *

def compute_error_for_given_points(b, m, points):
	#initialize error at 0
	totalError = 0;

	#for every point calculate error
	for i in range(0, len(points)):
		#get x value
		x = points[i, 0]
		#get y values
		y = points[i, 1]
		#get the difference, square it, add it to total
		totalError += (y - (m * x + b)) ** 2

	#get the average
	return totalError / float(len(points))

def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
	#starting b and m values
	b = starting_b
	m = starting_m

	#gradient descent
	for i in range(num_iterations):
		#update b and m with more accurate b and m by performing gradient decsent
		b, m = step_gradient(b, m, array(points), learning_rate)

	return [b, m]

def step_gradient(b_current, m_current, points, learning_rate):

	b_gradient = 0
	m_gradient = 0

	n = float(len(points))

	for i in range(0, len(points)):
		x = points[i, 0]
		y = points[i, 1]

		n = float(len(points))

		#direction w.r.t b and m
		#calculating partial derivative of our error function
		b_gradient += -(2/n) * (y - ((m_current * x) + b_current))
		m_gradient += -(2/n) * y * (y - ((m_current * x) + b_current))

	#update b  and m values
	new_b = b_current - (learning_rate * b_gradient)
	new_m = m_current - (learning_rate * m_gradient)
	return [new_b, new_m]



def run():

	#step 1 - collect your data
	points = genfromtxt('data.csv', delimiter=",")

	#step 2 - define our hyperparams
	learning_rate = 0.0001  #how fast our model converge?
	
	#y = mx + b
	initial_b = 0
	initial_m = 0
	num_iterations = 1000

	#step 3 - train  our model
	print("starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, compute_error_for_given_points(initial_b, initial_m, points)))
	[b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
	print("ending point at b = {1}, m = {2}, error = {3}".format(num_iterations, b, m, compute_error_for_given_points(b, m, points)))



if __name__ == '__main__':
	run()