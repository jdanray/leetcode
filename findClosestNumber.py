# https://leetcode.com/problems/find-closest-number-to-zero/ 

class Solution(object):
	def findClosestNumber(self, nums):
		res = float('inf')
		for n in nums:
			if abs(n) < abs(res) or (abs(n) == abs(res) and n > res):
				res = n
		return res
