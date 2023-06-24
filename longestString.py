# https://leetcode.com/problems/construct-the-longest-new-string/

class Solution(object):
	def longestString(self, x, y, z):
		@functools.lru_cache(None)
		def helper(x, y, z, prev):
			if prev == '':
				res = 0
				if x > 0:
					res = max(res, 2 + helper(x - 1, y, z, 'A'))
				if y > 0:
					res = max(res, 2 + helper(x, y - 1, z, 'B'))
				if z > 0:
					res = max(res, 2 + helper(x, y, z - 1, 'B'))
				return res
			elif prev == 'A':
				res = 0
				if y > 0:
					res = max(res, 2 + helper(x, y - 1, z, 'B'))
				return res
			elif prev == 'B':
				res = 0
				if x > 0:
					res = max(res, 2 + helper(x - 1, y, z, 'A'))
				if z > 0:
					res = max(res, 2 + helper(x, y, z - 1, 'B'))
				return res

		return helper(x, y, z, '')
