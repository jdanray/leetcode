# https://leetcode.com/problems/three-consecutive-odds/ 

class Solution(object):
	def threeConsecutiveOdds(self, arr):
		target = 3
		nodds = 0
		for n in arr:
			if n % 2 == 1:
				nodds += 1
			else:
				nodds = 0

			if nodds == target:
				return True

		return False
