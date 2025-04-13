# https://leetcode.com/problems/find-closest-person/

class Solution(object):
	def findClosest(self, x, y, z):
		one = abs(x - z)
		two = abs(y - z)
		return 1 if one < two else 2 if two < one else 0