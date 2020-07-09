# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/

class RandomizedCollection(object):
	def __init__(self):
		self.elems = collections.defaultdict(int)

	def insert(self, val):
		self.elems[val] += 1
		return self.elems[val] == 1
	
	def remove(self, val):
		if self.elems[val] > 0:
			self.elems[val] -= 1
			return True
		return False
    
	def getRandom(self):
		return random.choice([el for el in self.elems for _ in range(self.elems[el])])
