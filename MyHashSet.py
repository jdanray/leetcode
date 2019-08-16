# https://leetcode.com/problems/design-hashset/

class MyHashSet(object):
	def __init__(self):
		limit = 1000000
		self.table = [False for _ in range(limit + 1)]

	def add(self, key):
		self.table[key] = True

	def remove(self, key):
		self.table[key] = False

	def contains(self, key):
		return self.table[key]
