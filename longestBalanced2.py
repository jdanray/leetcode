# https://leetcode.com/problems/longest-balanced-subarray-i/

class Solution(object):
	def longestBalanced(self, nums):
		res = 0
		for i in range(len(nums)):
			seen = set()
			neven = 0
			nodd = 0
			for j in range(i, -1, -1):
				if nums[j] not in seen:
					if nums[j] % 2 == 0:
						neven += 1
					else:
						nodd += 1

				if neven == nodd:
					res = max(res, i - j + 1)

				seen.add(nums[j])

		return res