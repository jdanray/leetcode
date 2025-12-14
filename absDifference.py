# https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements/

class Solution(object):
	def absDifference(self, nums, k):
		nums = sorted(nums)
		a = sum(nums[:k])
		b = sum(nums[-k:])
		return abs(a - b)