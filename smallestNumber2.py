# https://leetcode.com/problems/construct-smallest-number-from-di-string/ 

class Solution(object):
	def smallestNumber(self, pattern):
		digits = '123456789'

		def backtrack(num):
			if len(num) == len(pattern) + 1:
				return [num]

			i = len(num) - 1
			res = []
			for d in digits:
				if not num or (d not in num and ((pattern[i] == 'I' and d > num[-1]) or (pattern[i] == 'D' and d < num[-1]))):
					res += backtrack(num + d)

			return res

		return min(backtrack(''))
