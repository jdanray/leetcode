# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/

class Solution(object):
	def numberOfArithmeticSlices(self, nums):
		res = 0
		ndiffs = collections.defaultdict(collections.Counter)
		for i in range(len(nums)):
			for j in range(i):
				d = nums[i] - nums[j]
				res += ndiffs[j][d]
				ndiffs[i][d] += ndiffs[j][d] + 1
                
		return res
