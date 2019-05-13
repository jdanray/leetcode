# https://leetcode.com/problems/partition-array-for-maximum-sum/

# Top-down DP
class Solution(object):
	def maxSumAfterPartitioning(self, A, K):
		memo = {}
		def dp(i):
			if i in memo:
				return memo[i]
	
			m = A[i]	
			s = A[i]
			soln = A[i]
			for k in range(K):
				if i + k < len(A):
					m = max(m, A[i + k])
					s = m * (k + 1)
					if i + k + 1 < len(A):
						s += dp(i + k + 1)
					soln = max(soln, s)

			memo[i] = soln
			return memo[i]

		return dp(0)

# Bottom-up DP
class Solution(object):
	def maxSumAfterPartitioning(self, A, K):
		dp = {}
		for i in range(len(A)):	
			m = A[i]	
			s = A[i]
			soln = A[i]
			for k in range(K):
				if i - k >= 0:
					m = max(m, A[i - k])
					s = m * (k + 1)
					if i - k - 1 >= 0:
						s += dp[i - k - 1]
					soln = max(soln, s)
			dp[i] = soln

		return dp[len(A) - 1]
