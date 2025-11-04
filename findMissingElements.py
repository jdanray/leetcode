# https://leetcode.com/problems/find-missing-elements/

class Solution(object):
	def findMissingElements(self, nums):
		nums = set(nums)

		minim = min(nums)
		maxim = max(nums)

		return [n for n in range(minim + 1, maxim) if n not in nums]