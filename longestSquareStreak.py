# https://leetcode.com/problems/longest-square-streak-in-an-array/ 

class Solution(object):
	def longestSquareStreak(self, nums):
		nums = sorted(nums)
		dp = collections.Counter()
		res = 1
		for n in nums:
			dp[n * n] = dp[n] + 1
			res = max(res, dp[n] + 1)

		return -1 if res == 1 else res

class Solution(object):
	def longestSquareStreak(self, nums):
		nums = sorted(nums)

		dp = collections.Counter()
		res = -1
		for n in nums:
			dp[n] = max(dp[n], dp[math.sqrt(n)] + 1)

			if dp[n] > 1 and dp[n] > res:
				res = dp[n]

		return res
