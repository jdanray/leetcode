# https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/

class Solution:
	def findLengthOfLCIS(self, nums):
		if not nums:
			return 0

		maxlen = 1
		curlen = 1
		for i in range(1, len(nums)):
			if nums[i] > nums[i - 1]:
				curlen += 1
			else:
				curlen = 1
			if curlen > maxlen:
				maxlen = curlen
		return maxlen
