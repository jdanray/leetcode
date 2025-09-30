# https://leetcode.com/problems/split-array-with-minimum-difference/

class Solution(object):
	def splitArray(self, nums):
		N = len(nums)

		rsum = [-1 for _ in range(N)]
		rsum[-1] = nums[-1]
		i = N - 2
		while i > 0 and nums[i] > nums[i + 1]:
			rsum[i] = rsum[i + 1] + nums[i]
			i -= 1

		lsum = 0
		i = 0
		res = float('inf')
		while i < N - 1 and (i == 0 or nums[i] > nums[i - 1]):
			lsum += nums[i]
			if rsum[i + 1] != -1:
				res = min(res, abs(lsum - rsum[i + 1]))
			i += 1

		return -1 if res == float('inf') else res