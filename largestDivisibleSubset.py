# https://leetcode.com/problems/largest-divisible-subset/ 

class Solution(object):
	def largestDivisibleSubset(self, nums):
		nums = sorted(nums)
		dp = [[i, 1] for i in range(len(nums))]
		globalMax = [0, 1]      # [index, size]
		for i, n in enumerate(nums):
			for j in range(i):
				if n % nums[j] == 0 and dp[j][1] + 1 > dp[i][1]:
					dp[i] = [j, dp[j][1] + 1]

				if dp[i][1] > globalMax[1]:
					globalMax = [i, dp[i][1]]

		i = globalMax[0]
		res = []
		while dp[i][0] != i:
			res.append(nums[i])
			i = dp[i][0]

		return res + [nums[i]]
