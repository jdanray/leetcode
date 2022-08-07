# https://leetcode.com/problems/number-of-arithmetic-triplets/ 

class Solution(object):
	def arithmeticTriplets(self, nums, diff):
		N = len(nums)

		res = 0
		for k in range(2, N):
			for j in range(1, k):
				for i in range(j):
					if nums[j] - nums[i] == nums[k] - nums[j] == diff:
						res += 1

		return res
