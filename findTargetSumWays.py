class Solution(object):
	def findTargetSumWays(self, nums, S):
		memo = {}
		def nways(i, acc):
			if i >= len(nums):
				return 1 if acc == S else 0

			if (i, acc) in memo:
				return memo[i, acc]

			memo[i, acc] = nways(i + 1, acc - nums[i]) + nways(i + 1, acc + nums[i])
			return memo[i, acc]
        
		return nways(0, 0)
