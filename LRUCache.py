# https://leetcode.com/problems/lru-cache/ 

class LRUCache(object):
	def __init__(self, capacity):
		self.capacity = capacity
		self.cache = collections.OrderedDict()

	def get(self, key):
		if key not in self.cache:
			return -1
		else:
			self.cache.move_to_end(key)
			return self.cache[key]

	def put(self, key, value):
		if len(self.cache) == self.capacity and key not in self.cache:
			self.cache.popitem(last=False)

		self.cache[key] = value
		self.cache.move_to_end(key)
