# https://leetcode.com/problems/online-stock-span/ 

class StockSpanner(object):
	def __init__(self):
		self.span = []
		self.prices = []

	def next(self, price):
		s = 1
		i = len(self.prices) - 1
		while i >= 0 and self.prices[i] <= price:
			s += self.span[i]
			i -= self.span[i] 

		self.prices.append(price)
		self.span.append(s)

		return s

"""
There is a more efficient way to solve this problem.
This problem is a version of a classic monostack problem.
""" 

class StockSpanner(object):
	def __init__(self):
		self.stack = []

	def next(self, price):
		res = 1
		while self.stack and self.stack[-1][0] <= price:
			_, s = self.stack.pop()
			res += s

		self.stack.append([price, res])
		return res
