'''
calculate fibonacci sequence using recursion
'''

#start
def fibonacci(x):
	if x == 1 or x == 2:
		return 1
	x = fibonacci(x-1) + fibonacci(x-2)
	return (x)
