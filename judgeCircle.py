# https://leetcode.com/problems/judge-route-circle/description/

class Solution:
	def judgeCircle(self, moves):
		pos = [0, 0]
		for m in moves:
			if m == 'U':
				pos[1] += 1
			elif m == 'D':
				pos[1] -= 1
			elif m == 'R':
				pos[0] += 1
			elif m == 'L':
				pos[0] -= 1
		return pos == [0, 0]
