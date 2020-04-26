# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

class Solution(object):
	def minStartValue(self, nums):
		total = 0
		minim = 0
		for n in nums:
			total += n
			minim = min(minim, total)
		return abs(minim) + 1
