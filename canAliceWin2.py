# https://leetcode.com/problems/stone-removal-game/

class Solution(object):
	def canAliceWin(self, n):
		s = 10
		p = False
		while n >= s:
			n -= s
			s -= 1
			p = not p

		return p