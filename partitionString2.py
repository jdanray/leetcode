# https://leetcode.com/problems/partition-string/

class Solution(object):
	def partitionString(self, s):
		seen = set()
		seg = ''
		res = []
		for c in s:
			seg += c
			if seg not in seen:
				seen.add(seg)
				res.append(seg)
				seg = ''
                
		return res