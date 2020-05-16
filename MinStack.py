# https://leetcode.com/problems/min-stack/

class MinStack(object):
	def __init__(self):
		self.stack = []
		self.minima = []

	def push(self, x):
		self.stack.append(x)
		if not self.minima or x <= self.minima[-1]:
			self.minima.append(x)

	def pop(self):
		if self.stack[-1] == self.minima[-1]:
			self.minima.pop()
		self.stack.pop()

	def top(self):
		return self.stack[-1]

	def getMin(self):
		return self.minima[-1]
