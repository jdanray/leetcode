# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

class Solution(object):
	def getSneakyNumbers(self, nums):
		seen = set()
		res = []
		for n in nums:
			if n in seen:
				res.append(n)
			seen.add(n)
		return res

class Solution(object):
	def getSneakyNumbers(self, nums):
		nums = sorted(nums)
		res = []
		for i in range(1, len(nums)):
			if nums[i] == nums[i - 1]:
				res.append(nums[i])
		return res