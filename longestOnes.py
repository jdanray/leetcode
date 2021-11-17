# https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution(object):
	def longestOnes(self, nums, k):
		i = 0
		res = 0
		for j, n in enumerate(nums):
			if n == 0:
				k -= 1

			while k < 0:
				if nums[i] == 0:
					k += 1
				i += 1

			res = max(res, j - i + 1)

		return res
