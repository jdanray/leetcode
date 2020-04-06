# https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/ 

class Solution(object):
	def minSubsequence(self, nums):
		nums = sorted(nums, reverse=True)
		total = sum(nums)
		s = 0
		res = []
		for n in nums:
			res.append(n)
			s += n
			if s > total - s:
				return res

class Solution(object):
	def minSubsequence(self, nums):
		count = collections.Counter(nums)
		start = max(count)
		total = sum(nums)
		s = 0
		res = []
		n = start
		while n >= 1:
			while count[n] > 0 and s <= total - s:
				count[n] -= 1
				s += n
				res.append(n)

			if s > total - s:
				return res
			else:
				n -= 1
