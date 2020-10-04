# https://leetcode.com/problems/crawler-log-folder/

class Solution(object):
	def minOperations(self, logs):
		res = 0
		for op in logs:
			if op == "../":
				res = max(0, res - 1)
			elif op != "./":
				res += 1
		return res
