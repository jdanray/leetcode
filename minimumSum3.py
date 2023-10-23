# https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/ 

class Solution(object):
	def minimumSum(self, nums):
		N = len(nums)

		minLeft = [float('inf') for _ in range(N)]
		for i in range(1, N):
			minLeft[i] = min(minLeft[i - 1], nums[i - 1])

		minRight = nums[-1]
		res = float('inf')
		for j in range(N - 2, 0, -1):
			if minLeft[j] < nums[j] and minRight < nums[j]:
				res = min(res, minLeft[j] + nums[j] + minRight)

			minRight = min(minRight, nums[j])

		return -1 if res == float('inf') else res
