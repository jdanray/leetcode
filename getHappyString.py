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
			
class Solution(object):
	def getHappyString(self, n, k):
		chars = 'abc'

		queue = ['']
		res = ''
		while queue:
			s = queue.pop(0)

			if len(s) == n:
				res = s
				k -= 1

				if k == 0:
					return res
				else:
					continue

			for c in chars:
				if not s or c != s[-1]:
					queue.append(s + c)

		return ''
