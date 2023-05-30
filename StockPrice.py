# https://leetcode.com/problems/stock-price-fluctuation/ 

from sortedcontainers import SortedList

class StockPrice(object):
	def __init__(self):
		self.maxTime = 0
		self.prices = SortedList()
		self.timePrice = dict()

	def update(self, timestamp, price):
		if timestamp in self.timePrice:
			self.prices.remove(self.timePrice[timestamp])

		self.timePrice[timestamp] = price
		self.prices.add(price)

		if timestamp > self.maxTime:
			self.maxTime = timestamp

	def current(self):
		return self.timePrice[self.maxTime]

	def maximum(self):
		return self.prices[-1]

	def minimum(self):
		return self.prices[0]
