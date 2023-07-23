# https://leetcode.com/problems/check-if-array-is-good/ 

class Solution(object):
	def isGood(self, nums):
		count = collections.Counter(nums)
		n = len(nums) - 1
		return count[n] == 2 and all(count[x] == 1 for x in range(1, n))
