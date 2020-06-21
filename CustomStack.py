# https://leetcode.com/problems/design-a-stack-with-increment-operation/ 

class CustomStack(object):
	def __init__(self, maxSize):
		self.maxsize = maxSize
		self.stack = []

	def push(self, x):
		if len(self.stack) < self.maxsize:
			self.stack.append(x)

	def pop(self):
		if not self.stack:
			return -1
		else:
			return self.stack.pop()

	def increment(self, k, val):
		for i in range(min(k, len(self.stack))):
			self.stack[i] += val
