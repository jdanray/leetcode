# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/ 

class Solution(object):
	def minPartitions(self, n):
		res = 0
		for d in n:
			res = max(res, int(d))
		return res
