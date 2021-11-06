# https://leetcode.com/problems/rle-iterator/ 

class RLEIterator(object):
	def __init__(self, encoding):
		self.encoding = encoding
		self.idx = 0

	def next(self, n):
		while self.idx < len(self.encoding) and self.encoding[self.idx] < n:
			n -= self.encoding[self.idx]
			self.idx += 2

		if self.idx >= len(self.encoding):
			return -1

		self.encoding[self.idx] -= n
		return self.encoding[self.idx + 1]
