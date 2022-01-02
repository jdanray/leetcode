# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution(object):
	def numberOfBeams(self, bank):
		prevRow = 0
		res = 0
		for r in bank:
			curRow = r.count('1')            
			if curRow > 0:
				res += prevRow * curRow
				prevRow = curRow

		return res
