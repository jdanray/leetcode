# https://leetcode.com/problems/design-memory-allocator/

class Allocator(object):
	def __init__(self, n):
		self.memory = [0 for _ in range(n)]

	def allocate(self, size, mID):
		s = 0
		for i in range(len(self.memory)):
			if self.memory[i] == 0:
				s += 1
			else:
				s = 0

			if s == size:
				start = i - size + 1
				for j in range(start, i + 1):
					self.memory[j] = mID
				return start

		return -1

	def free(self, mID):
		res = 0
		for i in range(len(self.memory)):
			if self.memory[i] == mID:
				self.memory[i] = 0
				res += 1
		return res