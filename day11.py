"""Instructions

6x6 array has 16 hourglasses

An hourglass sum is the sum of the numbers in the hourglass

Calculate hourglass sum for all hourglasses and find max

Input is 6 strings of integers

Inclusive range -9 to 9

You need to treat the first 4 rows as the first row, first 4 columns as starting pts"""

def get_sum(lst):
	max_sum = 0
	for i in range(0,4):
		for j in range(0,4):
			current_sum = (arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + 
						   arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])

			max_sum = max(max_sum, current_sum)

	print max_sum




