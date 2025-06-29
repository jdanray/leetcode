# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

class Solution(object):
	def numSubseq(self, nums, target):
		MOD = 10**9 + 7

		nums = sorted(nums)
		j = len(nums) - 1
		res = 0
		for i in range(len(nums)):
			while nums[i] + nums[j] > target and j > i:
				j -= 1
			
			if nums[i] + nums[j] <= target:
				res += 2 ** (j - i)

		return res % MOD

class Solution(object):
	def numSubseq(self, nums, target):
		MOD = 10**9 + 7

		nums = sorted(nums)
		i = 0
		j = len(nums) - 1
		res = 0
		while i <= j:
			if nums[i] + nums[j] <= target:
				res += 2 ** (j - i)
				i += 1
			else:
				j -= 1

		return res % MOD