# https://leetcode.com/problems/combination-sum-iii/

class Solution:
	def combinationSum3(self, k, n, combo=[], start=1):
		if k == 0:
			return [combo] if n == 0 else []

		res = []
		for i in range(start, 9 + 1):
			res += self.combinationSum3(k - 1, n - i, combo + [i], i + 1)
		return res

class Solution(object):
	def combinationSum3(self, k, n):
		def helper(start, k, n, combo):
			if k == 0 and n == 0:
				return [combo]
			elif k == 0 or n <= 0:
				return []

			res = []
			for num in range(start, 10):
				res += helper(num, k - 1, n - num, combo + [num])
			return res

		return helper(1, k, n, [])

class Solution(object):
	def combinationSum3(self, k, n):
		if k <= 0 or n <= 0:
			return []
		else:
			return self._combinationSum3(k, n)

	def _combinationSum3(self, k, n, s=[], i=1):
		if n == 0 and len(s) == k:
			return [s]
		elif n < 0:
			return []

		solutions = []
		for j in range(i, 10):
			solutions += self._combinationSum3(k, n - j, s + [j], j + 1)
		return solutions
