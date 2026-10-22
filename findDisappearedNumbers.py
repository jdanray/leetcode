# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/ 

class Solution(object):
	def findDisappearedNumbers(self, nums):
		N = len(nums)
		nums = set(nums)
		return [n for n in range(1, N + 1) if n not in nums]
