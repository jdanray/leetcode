# https://leetcode.com/problems/design-an-ordered-stream/ 

class OrderedStream(object):
	def __init__(self, n):
		self.ptr = 1
		self.idvals = {}

	def insert(self, id, value):
		self.idvals[id] = value

		if self.ptr != id:
			return []

		res = []
		while id in self.idvals:
			res.append(self.idvals[id])
			id += 1
			
		self.ptr = id
		return res
