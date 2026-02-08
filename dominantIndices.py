# https://leetcode.com/problems/count-dominant-indices/

class Solution(object):
	def dominantIndices(self, nums):
		N = len(nums)

		s = 0.0
		avg = 0.0
		count = 0
		for i in range(N - 1, -1, -1):
			if i < N - 1 and nums[i] > avg:
				count += 1

			s += nums[i]
			avg = s / (N - i)

		return count