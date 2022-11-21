# https://leetcode.com/problems/number-of-unequal-triplets-in-array/

class Solution(object):
	def unequalTriplets(self, nums):
		N = len(nums)

		res = 0
		for i in range(N - 2):
			for j in range(i + 1, N - 1):
				for k in range(j + 1, N):
					if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
						res += 1

		return res
