# https://leetcode.com/problems/apply-discount-every-n-orders/

class Cashier(object):
	def __init__(self, n, discount, products, prices):
		self.N = n
		self.ncustomers = 0
		self.discount = discount
		self.price = {prod: prices[i] for i, prod in enumerate(products)}

	def getBill(self, product, amount):
		cost = 0.0
		for i, prod in enumerate(product):
			cost += self.price[prod] * amount[i]

		self.ncustomers += 1
		if self.ncustomers % self.N == 0:
			cost -= (self.discount * cost) / 100

		return cost 
