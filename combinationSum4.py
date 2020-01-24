# https://leetcode.com/problems/combination-sum-iv/ 

class Solution(object):
	def combinationSum4(self, nums, target):
		memo = {}

		def helper(t):
			if t == 0:
				return 1
			elif t < 0:
				return 0
			elif t in memo:
				return memo[t]

			memo[t] = 0
			for n in nums:
				memo[t] += helper(t - n)
			return memo[t]

		return helper(target)

class Solution(object):
	def combinationSum4(self, nums, target):
		memo = [0 for _ in range(target + 1)]
		memo[0] = 1
		for t in range(1, target + 1):
			for n in nums:
				if t - n >= 0:
					memo[t] += memo[t - n]
		return memo[target]
