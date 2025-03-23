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

class Solution(object):
	def smallestNumber(self, pattern):
		digits = list(range(1, 10))

		queue = [[[], set()]]
		while queue:
			num, used = queue.pop(0)

			if len(num) == len(pattern) + 1:
				return ''.join(str(d) for d in num)

			for d in digits:
				if d not in used and (not num or (pattern[len(num) - 1] == 'I' and d > num[-1]) or (pattern[len(num) - 1] == 'D' and d < num[-1])):
					queue.append([num + [d], used | {d}])

		return ''
