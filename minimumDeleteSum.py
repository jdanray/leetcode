# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

class Solution(object):
	def minimumDeleteSum(self, s1, s2):
		asc1 = [0]
		for i, c in enumerate(s1):
			asc1.append(asc1[i] + ord(c))

		asc2 = [0] 
		for i, c in enumerate(s2):
			asc2.append(asc2[i] + ord(c)) 

		m = len(s1)
		n = len(s2)
		memo = {}
		def helper(m, n):
			if m == 0:
				return asc2[n]
			elif n == 0:
				return asc1[m]

			if (m, n) in memo:
				return memo[m, n]

			if s1[m - 1] == s2[n - 1]:
				memo[m, n] = helper(m - 1, n - 1)
				return memo[m, n]

			memo[m, n] = min(helper(m - 1, n) + asc1[m] - asc1[m - 1], helper(m, n - 1) + asc2[n] - asc2[n - 1])
			return memo[m, n]

		return helper(m, n)
