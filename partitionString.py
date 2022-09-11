# https://leetcode.com/problems/optimal-partition-of-string/ 

class Solution(object):
	def partitionString(self, s):
		res = 1
		seen = set()
		for c in s:
			if c in seen:
				res += 1
				seen = set()

			seen.add(c)

		return res
