# https://leetcode.com/problems/longest-nice-subarray/ 

class Solution(object):
	def longestNiceSubarray(self, nums):
		window = 0
		i = 0
		res = 0
		for j, n in enumerate(nums):
			while window & n != 0:
				window ^= nums[i]
				i += 1

			window |= n
			res = max(res, j - i + 1)

		return res
