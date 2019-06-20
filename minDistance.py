# https://leetcode.com/problems/edit-distance/

# Bottom-up DP
class Solution:
	def minDistance(self, word1, word2):
		m = len(word1)
		n = len(word2)
		memo = {}
		for i in range(m + 1):
			for j in range(n + 1):
				if i == 0:
					memo[i, j] = j
				elif j == 0:
					memo[i, j] = i
				elif word1[i - 1] == word2[j - 1]:
					memo[i, j] = memo[i - 1, j - 1]
				else:
					memo[i, j] = 1 + min(memo[i - 1, j], memo[i, j - 1], memo[i - 1, j - 1])
                    
		return memo[m, n]

# Top-down DP
class Solution:
	def minDistance(self, word1, word2):
		m = len(word1)
		n = len(word2)
		memo = {}
		def helper(m, n):
			if m == 0:
				return n
			elif n == 0:
				return m

			if (m, n) in memo:
				return memo[m, n]

			if word1[m - 1] == word2[n - 1]:
				memo[m, n] = helper(m - 1, n - 1)
				return memo[m, n]

			memo[m, n] = 1 + min(helper(m - 1, n), helper(m, n - 1), helper(m - 1, n - 1))
			return memo[m, n]

		return helper(m, n)
