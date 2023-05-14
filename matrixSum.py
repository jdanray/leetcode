# https://leetcode.com/problems/sum-in-a-matrix/ 

class Solution(object):
	def matrixSum(self, nums):
		M = len(nums)
		N = len(nums[0])

		nums = [sorted(row, reverse=True) for row in nums]

		res = 0
		for j in range(N):
			res += max(nums[i][j] for i in range(M))

		return res
