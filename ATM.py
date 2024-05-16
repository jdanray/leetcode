# https://leetcode.com/problems/design-an-atm-machine/ 

class ATM(object):
	def __init__(self):
		self.denom = [20, 50, 100, 200, 500]
		self.bank = [0 for _ in range(len(self.denom))]

	def deposit(self, banknotesCount):
		for i, b in enumerate(banknotesCount):
			self.bank[i] += b

	def withdraw(self, amount):
		res = [0 for _ in range(len(self.denom))]
		for i in range(len(self.denom) - 1, -1, -1):
			d = min(self.bank[i], amount // self.denom[i])
			amount -= d * self.denom[i]
			res[i] = d

		if amount > 0:
			return [-1]
		else:
			self.deposit([-r for r in res])
			return res
