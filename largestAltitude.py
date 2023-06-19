# https://leetcode.com/problems/find-the-highest-altitude/ 

class Solution(object):
	def largestAltitude(self, gain):
		alt = 0
		res = 0
		for g in gain:
			alt += g
			res = max(res, alt)
		return res

class Solution(object):
	def largestAltitude(self, gain):
		return max(0, max(itertools.accumulate(gain)))
