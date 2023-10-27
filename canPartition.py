# https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
	def canPartition(self, nums):
		total = sum(nums)

		if total % 2 == 1:
			return False

		total //= 2

		can = collections.defaultdict(bool)
		can[0] = True
		for n in nums:
			for s in range(total, 0, -1):
				can[s] |= can[s - n]

		return can[total]

class Solution(object):
	def canPartition(self, nums):
		sumNums = sum(nums)

		memo = {}
		def dp(i, s):
			if i >= len(nums):
				return s == sumNums - s

			if (i, s) in memo:
				return memo[i, s]

			memo[i, s] = dp(i + 1, s + nums[i]) or dp(i + 1, s)
			return memo[i, s]

		return dp(0, 0)
