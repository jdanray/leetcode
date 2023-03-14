# https://leetcode.com/problems/interleaving-string/ 

class Solution(object):
	def isInterleave(self, s1, s2, s3):
		memo = {}
		def dp(i, j, k):
			if k >= len(s3):
				return i >= len(s1) and j >= len(s2)

			if (i, j, k) in memo:
				return memo[i, j, k]

			if i < len(s1) and s1[i] == s3[k] and dp(i + 1, j, k + 1):
				memo[i, j, k] = True
			elif j < len(s2) and s2[j] == s3[k] and dp(i, j + 1, k + 1):
				memo[i, j, k] = True
			else:
				memo[i, j, k] = False

			return memo[i, j, k]

		return dp(0, 0, 0)

"""
After I solve a problem, I like to study other people's solutions. The following solution showed me how to reduce the complexity of my solution:

https://leetcode.com/problems/interleaving-string/discuss/1247165/C%2B%2B-Memoizn(3-variables)-greater-Memoizn(without-3rd-var)-greater-DP-(m*n)-greater-DP(n)

I modified my code accordingly: 
"""

class Solution(object):
	def isInterleave(self, s1, s2, s3):
		memo = {}
		def dp(i, j):
			if i + j >= len(s3):
				return i >= len(s1) and j >= len(s2)

			if (i, j) in memo:
				return memo[i, j]

			if i < len(s1) and s1[i] == s3[i + j] and dp(i + 1, j):
				memo[i, j] = True
			elif j < len(s2) and s2[j] == s3[i + j] and dp(i, j + 1):
				memo[i, j] = True
			else:
				memo[i, j] = False

			return memo[i, j]

		return dp(0, 0)
