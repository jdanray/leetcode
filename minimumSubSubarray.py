# https://leetcode.com/problems/minimum-positive-sum-subarray/

class Solution(object):
	def minimumSumSubarray(self, nums, l, r):
		N = len(nums)

		res = float('inf')
		for i in range(N):
			s = 0
			for j in range(i, min(i + r, N)):
				s += nums[j]
				if j - i + 1 >= l and s > 0:
					res = min(res, s)

		return res if res != float('inf') else -1