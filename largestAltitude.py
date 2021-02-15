# https://leetcode.com/problems/find-the-highest-altitude/ 

class Solution(object):
	def largestAltitude(self, gain):
		res = 0
		alt = 0		
		for g in gain:
			alt += g
			res = max(res, alt)
		return res
