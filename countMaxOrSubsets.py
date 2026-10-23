# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

class Solution(object):
	def countMaxOrSubsets(self, nums):
		stack = [[0, 0]]
		maxOr = 0
		res = 0
		while stack:
			i, s = stack.pop()

			if i >= len(nums):
				continue

			stack.append([i + 1, s])

			s |= nums[i]
            
			if s > maxOr:
				maxOr = s
				res = 0

			if s == maxOr:
				res += 1

			stack.append([i + 1, s])

		return res