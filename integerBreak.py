# https://leetcode.com/problems/integer-break/description/

class Solution(object):
	def integerBreak(self, n):
		memo = {1: 1, 2: 1}
		def intbreak(n):
			if n not in memo:
				memo[n] = 0
				for s1 in range(1, (n // 2) + 1):
					s2 = n - s1
					p1 = s1 * s2
					p2 = intbreak(s1) * s2
					p3 = s1 * intbreak(s2)
					memo[n] = max(memo[n], p1, p2, p3)
			return memo[n]
		return intbreak(n)

class Solution(object):
	def integerBreak(self, N):
		memo = {1: 1, 2: 1}
		for n in range(3, N + 1):
			memo[n] = 0
			for s1 in range(1, (n // 2) + 1):
				s2 = n - s1
				p1 = s1 * s2
				p2 = memo[s1] * s2
				p3 = s1 * memo[s2]
				memo[n] = max(memo[n], p1, p2, p3)
		return memo[N]
