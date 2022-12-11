# https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/ 

class Solution(object):
	def maximumValue(self, strs):
		res = 0
		for s in strs:
			if s.isnumeric():
				res = max(res, int(s))
			else:
				res = max(res, len(s))
                
		return res
