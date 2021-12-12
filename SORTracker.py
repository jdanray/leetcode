# https://leetcode.com/problems/sequentially-ordinal-rank-tracker/

from sortedcontainers import SortedList

class SORTracker(object):
	def __init__(self):
		self.q = 0
		self.items = SortedList()

	def add(self, name, score):
		self.items.add((-score, name))

	def get(self):
		res = self.items[self.q][1]
		self.q += 1
		return res
