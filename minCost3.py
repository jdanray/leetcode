# https://leetcode.com/problems/minimum-cost-to-split-an-array/

class Solution(object):
	def minCost(self, nums, k):
		N = len(nums)

		memo = {}
		def dp(start):
			if start >= N:
				return 0

			if start in memo:
				return memo[start]

			count = [0] * 1001
			t = 0
			res = float('inf')
			for i in range(start, N):
				n = nums[i]
				if count[n] == 1:
					t += 2
				elif count[n] > 1:
					t += 1
				count[n] += 1

				res = min(res, t + k + dp(i + 1))

			memo[start] = res
			return memo[start]

		return dp(0)
