# https://leetcode.com/problems/missing-number/ 

class Solution(object):
	def missingNumber(self, nums):
		return sum(range(len(nums) + 1)) - sum(nums)

class Solution(object):
	def missingNumber(self, nums):
		n = len(nums)
		s = (n * (n + 1)) / 2
		return s - sum(nums)

class Solution:
	def missingNumber(self, nums):
		c = [0 for _ in range(len(nums) + 1)]
		for n in nums:
			c[n] = 1
		for m in range(len(nums) + 1):
			if c[m] == 0:
				return m

class Solution(object):
	def missingNumber(self, nums):
		nums = set(nums)
		for n in range(len(nums) + 1):
			if n not in nums:
				return n
