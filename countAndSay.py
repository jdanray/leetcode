# https://leetcode.com/problems/count-and-say/ 

class Solution(object):
	def countAndSay(self, n):
		if n == 1:
			return '1'

		prev = '1'
		for _ in range(n - 1):
			l = len(prev)
			i = 0
			res = ''
			while i < l:
				c = 1
				while i + 1 < l and prev[i] == prev[i + 1]:
					c += 1
					i += 1

				res += str(c) + prev[i - c + 1]
				i += 1

			prev = res

		return res
