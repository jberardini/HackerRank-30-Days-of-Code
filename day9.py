N = input()

def factorial(N):
	if N == 0:
		return 1

	result = N * factorial(N-1)

	return result


print factorial(N)