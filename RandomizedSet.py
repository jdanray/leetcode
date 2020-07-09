# https://leetcode.com/problems/insert-delete-getrandom-o1/

class RandomizedSet(object):
	def __init__(self):
		self.elems = set()

	def insert(self, val):
		if val not in self.elems:
			self.elems.add(val)
			return True

		return  False
	
	def remove(self, val):
		if val in self.elems:
			self.elems.remove(val)
			return True

		return False
    
	def getRandom(self):
		return random.choice(list(self.elems))
