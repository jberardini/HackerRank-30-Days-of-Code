"""Notes

class constructor: takes an array and saves it to elements instance variable
computeDifference method that finds maximum absolute difference and stores as maximumDifference
instance variable.
"""

class Difference(object):
	def __init__(self, elements):
		self.elements = elements
		self.maximumDifference = None
		self.largest = self.elements[0]
		self.smallest = self.elements[0]

	def computeDifference(self):
		for element in self.elements:
			self.largest = max(self.largest, element)
			self.smallest = min(self.smallest, element)

		self.maximumDifference = abs(self.largest - self.smallest)
		return self.maximumDifference

example1 = Difference([8, 2, 10])

print example1.computeDifference()



