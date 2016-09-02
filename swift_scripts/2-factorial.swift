// Uses a loop from 1 to N, multiplying each n from 1 to N
func factorial(N: Int) -> (Int) {
	if N <= 1 {
		return 1
	}

	var factorial = 1

	for i in 1...N {
		factorial = factorial * i
	}
	return factorial
}
