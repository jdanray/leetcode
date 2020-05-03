# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/ 

class Solution(object):
	def kLengthApart(self, nums, k):
		z = 0
		for i, n in enumerate(nums):
			if n == 0:
				z += 1
			elif z < k and i != 0:
				return False
			else:
				z = 0
		return True
