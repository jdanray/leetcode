# https://leetcode.com/problems/combination-sum-iii/

class Solution:
	def combinationSum3(self, k, n, combo=[], start=1):
		if k == 0:
			return [combo] if n == 0 else []

		res = []
		for i in range(start, 9 + 1):
			res += self.combinationSum3(k - 1, n - i, combo + [i], i + 1)
		return res
