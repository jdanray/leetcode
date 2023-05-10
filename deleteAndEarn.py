# https://leetcode.com/problems/delete-and-earn/ 

class Solution(object):
	def deleteAndEarn(self, nums):
		count = collections.Counter(nums)
		keys = sorted(count.keys())
		n = len(keys)

		dp = [0 for _ in range(n)]
		for i in range(n):
			leave = 0
			take = keys[i] * count[keys[i]]

			if i - 1 >= 0:
				leave = dp[i - 1]
				if keys[i - 1] != keys[i] - 1:
					take += dp[i - 1]
				elif i - 2 >= 0:
					take += dp[i - 2]

			dp[i] = max(leave, take)

		return max(dp)
