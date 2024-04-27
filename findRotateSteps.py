# https://leetcode.com/problems/freedom-trail/ 

class Solution(object):
	def findRotateSteps(self, ring, key):
		memo = {}
		def dp(i, j):
			if i >= len(key):
				return 0

			if (i, j) in memo:
				return memo[i, j]

			res = float('inf')
			for k in range(len(ring)):
				for d in [k, -k]:
					l = (j + d) % len(ring)
					if ring[l] == key[i]:
						res = min(res, k + 1 + dp(i + 1, l))

			memo[i, j] = res
			return memo[i, j]

		return dp(0, 0)
