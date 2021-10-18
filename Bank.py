# https://leetcode.com/problems/simple-bank-system/ 

class Bank(object):
	def __init__(self, balance):
		self.balance = balance

	def isValidAccount(self, account):
		return 1 <= account <= len(self.balance)

	def transfer(self, account1, account2, money):
		if not self.withdraw(account1, money):
			return False
		elif not self.deposit(account2, money):
			self.deposit(account1, money)
			return False
		else:
			return True

	def deposit(self, account, money):
		if self.isValidAccount(account):
			self.balance[account - 1] += money
			return True
		else:
			return False

	def withdraw(self, account, money):
		if self.isValidAccount(account) and self.balance[account - 1] >= money:
			self.balance[account - 1] -= money
			return True
		else: 
			return False
