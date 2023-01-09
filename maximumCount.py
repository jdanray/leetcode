# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

class Solution(object):
	def maximumCount(self, nums):
		neg = 0
		pos = 0
		for n in nums:
			if n < 0:
				neg += 1
			elif n > 0:
				pos += 1

		return max(neg, pos)

class Solution(object):
	def maximumCount(self, nums):
		N = len(nums)

		i = 0
		n = 0
		while i < N and nums[i] <= 0:
			if nums[i] < 0:
				n += 1
			i += 1

		return max(n, N - n)
