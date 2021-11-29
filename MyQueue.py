# https://leetcode.com/problems/implement-queue-using-stacks/ 

class MyQueue(object):
	def __init__(self):
		self.A = []
		self.B = []

	def push(self, x):
		self.A.append(x)

	def pop(self):
		if not self.B:
			self.transfer()            
		return self.B.pop()

	def peek(self):
		if not self.B:
			self.transfer()            
		return self.B[-1]

	def empty(self):
		return not self.A and not self.B

	def transfer(self):
		while self.A:
			a = self.A.pop()
			self.B.append(a)
