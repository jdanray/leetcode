# https://leetcode.com/problems/random-pick-index/ 

class Solution(object):
	def __init__(self, nums):
		self.indexes = collections.defaultdict(list)
		for i, n in enumerate(nums):
			self.indexes[n].append(i)
	
	def pick(self, target):
		return random.choice(self.indexes[target])
