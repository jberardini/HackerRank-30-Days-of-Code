class Solution(object):
	def __init__(self):
		self.my_stack = []
		self.my_queue = []

	def enqueueCharacter(self, item):
		self.my_queue.append(item)

	def dequeueCharacter(self):
		return self.my_queue.pop(0)

	def pushCharacter(self, item):
		self.my_stack.append(item)

	def popCharacter(self):
		return self.my_stack.pop()