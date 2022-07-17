# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/ 

class Solution(object):
	def maximumSum(self, nums):
		res = -1
		maxim = {}
		for i, n in enumerate(nums):
			s = 0
			x = n
			while x > 0:
				s += x % 10
				x //= 10

			if s in maxim:
				res = max(res, maxim[s] + n)
				maxim[s] = max(maxim[s], n)
			else:
				maxim[s] = n 

		return res 
