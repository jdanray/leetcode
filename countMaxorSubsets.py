# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

class Solution(object):
	def countMaxOrSubsets(self, nums):
		def bitwiseOr(sub): 
			return functools.reduce(lambda a, b: a | b, sub)
 
		maxOr = bitwiseOr(nums)
		res = 0
		for r in range(1, len(nums) + 1):
			for sub in itertools.combinations(nums, r):
				if bitwiseOr(sub) == maxOr:
					res += 1

		return res
