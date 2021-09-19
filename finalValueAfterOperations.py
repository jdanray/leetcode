# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/ 

class Solution(object):
	def finalValueAfterOperations(self, operations):
		d = {}
		d["++X"] = 1
		d["X++"] = 1
		d["--X"] = -1
		d["X--"] = -1

		return sum(d[op] for op in operations)
