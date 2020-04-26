# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

class Solution(object):
	def getHappyString(self, n, k):
		succs = {'a': 'bc', 'b': 'ac', 'c': 'ab'}
		def generate(n):
			if n == 1:
				return ['a', 'b', 'c']

			res = []
			prev = generate(n - 1)
			for p in prev:
				for l in succs[p[-1]]:
					res.append(p + l)
			return res

		if k > 3 * 2 ** (n - 1):
			return ""
		else:
			return generate(n)[k - 1]
