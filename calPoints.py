# https://leetcode.com/problems/baseball-game/

class Solution:
	def calPoints(self, ops):
		valid = []
		for c in ops:
			if c == '+':
				valid.append(valid[-1] + valid[-2])
			elif c == 'D':
				valid.append(valid[-1] + valid[-1])
			elif c == 'C':
				valid.pop()
			else:
				valid.append(int(c)) 
		return sum(valid)
