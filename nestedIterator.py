# https://leetcode.com/problems/flatten-nested-list-iterator/description/

class NestedIterator(object):
	def __init__(self, nestedList):
		self.lst = []
		self.flatten(nestedList)
	
	def flatten(self, nestedList):
		for u in nestedList:
			if u.isInteger():
				self.lst.append(u.getInteger())
			else:
				self.flatten(u.getList())

	def next(self):
		return self.lst.pop(0)

	def hasNext(self):
		return len(self.lst) > 0
