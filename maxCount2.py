# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/

class Solution(object):
	def maxCount(self, banned, n, maxSum):
		banned = set(banned)

		s = 0
		res = 0
		for num in range(1, n + 1):
			if s + num > maxSum:
				return res

			if num not in banned:
				s += num
				res += 1

		return res
