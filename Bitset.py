# https://leetcode.com/problems/design-bitset/ 

class Bitset(object):
	def __init__(self, size):
		self.bits = [0 for _ in range(size)]
		self.ones = 0
		self.flipped = False

	def fix(self, idx):
		if self.flipped and self.bits[idx] == 1:
			self.ones -= 1
			self.bits[idx] = 0
		elif not self.flipped and self.bits[idx] == 0:
			self.ones += 1
			self.bits[idx] = 1

	def unfix(self, idx):
		if self.flipped and self.bits[idx] == 0:
			self.ones += 1
			self.bits[idx] = 1
		elif not self.flipped and self.bits[idx] == 1:
			self.ones -= 1
			self.bits[idx] = 0

	def flip(self):
		self.flipped = not self.flipped

	def all(self):
		return self.count() == len(self.bits)

	def one(self):
		return self.count() > 0

	def count(self):
		if self.flipped:
			return len(self.bits) - self.ones
		else:
			return self.ones

	def toString(self):
		if self.flipped:
			return ''.join('1' if b == 0 else '0' for b in self.bits)
		else:
			return ''.join('0' if b == 0 else '1' for b in self.bits)
