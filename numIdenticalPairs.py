# https://leetcode.com/problems/number-of-good-pairs/ 

class Solution(object):
	def numIdenticalPairs(self, nums):
		count = collections.defaultdict(int)
		res = 0
		for n in nums:
			res += count[n]
			count[n] += 1
		return res
