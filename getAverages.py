# https://leetcode.com/problems/k-radius-subarray-averages/ 

class Solution(object):
	def getAverages(self, nums, k):
		N = len(nums)

		k2 = k * 2
		res = [-1 for _ in range(N)]
		s = 0
		for i in range(N):
			s += nums[i]

			if i >= k2:
				res[i - k] = s / (k2 + 1)
				s -= nums[i - k2]

		return res
