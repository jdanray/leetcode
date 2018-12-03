# https://leetcode.com/contest/weekly-contest-111/problems/di-string-match/

class Solution(object):
	def diStringMatch(self, S):
		p = []
		i = 0
		d = len(S)
		for c in S:
			if c == 'D':
				p.append(d)
				d -= 1
			elif c == 'I':
				p.append(i)
				i += 1
		return p + [d]
