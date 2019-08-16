# https://leetcode.com/problems/design-hashmap/

class MyHashMap(object):
	def __init__(self):
		limit = 1000000
		self.table = [-1 for _ in range(limit + 1)]

	def put(self, key, value):
		self.table[key] = value

	def get(self, key):
		return self.table[key]

	def remove(self, key):
		self.table[key] = -1
