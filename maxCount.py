# https://leetcode.com/problems/range-addition-ii/

class Solution(object):
	def maxCount(self, m, n, ops):
		if not ops:
			return m * n

		a = ops[0][0]
		b = ops[0][1]
		for i in range(1, len(ops)):
			a = min(a, ops[i][0])
			b = min(b, ops[i][1])

		return a * b

class Solution(object):
	def maxCount(self, m, n, ops):
		for a, b in ops:
			m = min(m, a)
			n = min(n, b)
		return m * n

class Solution(object):
	def maxCount(self, m, n, ops):
		if not ops:
			return m * n

		return min(o[0] for o in ops) * min(o[1] for o in ops)
