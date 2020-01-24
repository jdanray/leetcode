# https://leetcode.com/problems/combination-sum/ 

class Solution(object):
	def combinationSum(self, candidates, target):
		def helper(start, t, combo):
			if t == 0:
				return [combo]
			elif t < 0:
				return []

			res = []
			for i in range(start, len(candidates)):
				res += helper(i, t - candidates[i], combo + [candidates[i]])
			return res

		return helper(0, target, [])
