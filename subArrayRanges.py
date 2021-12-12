# https://leetcode.com/problems/sum-of-subarray-ranges/ 

class Solution(object):
	def subArrayRanges(self, nums):
		N = len(nums)

		res = 0
		for i in range(N):
			maxi = float('-inf')
			mini = float('inf')
			r = 0
			for j in range(i, N):
				maxi = max(maxi, nums[j])
				mini = min(mini, nums[j])
				r = maxi - mini
				res += r

		return res
