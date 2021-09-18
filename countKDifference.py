# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/ 

class Solution(object):
	def countKDifference(self, nums, k):
		N = len(nums)

		res = 0
		for j in range(N):
			for i in range(j):
				if abs(nums[i] - nums[j]) == k:
					res += 1

		return res
