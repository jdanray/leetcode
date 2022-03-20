# https://leetcode.com/problems/divide-array-into-equal-pairs/ 

class Solution(object):
	def divideArray(self, nums):
		return all(c % 2 == 0 for c in collections.Counter(nums).values())
