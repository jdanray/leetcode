# https://leetcode.com/problems/furthest-point-from-origin/ 

class Solution(object):
	def furthestDistanceFromOrigin(self, moves):
		l = moves.count('L')
		r = moves.count('R')
		b = moves.count('_')
		return b + max(l, r) - min(l, r)
