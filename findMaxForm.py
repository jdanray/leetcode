# https://leetcode.com/problems/ones-and-zeroes/

class Solution(object):
	def findMaxForm(self, strs, m, n):
		count = {i: collections.Counter(s) for i, s in enumerate(strs)}
		memo = {}
		def dp(m, n, i):
			if (m, n, i) in memo:
				return memo[m, n, i]

			if i >= len(strs):
				return 0

			skip = dp(m, n, i + 1)
            
			zeroes = count[i]['0']
			ones = count[i]['1']    
            
			if zeroes > m or ones > n:
				memo[m, n, i] = skip
				return memo[m, n, i]

			keep = dp(m - zeroes, n - ones, i + 1)
			memo[m, n, i] = max(skip, keep + 1)
			return memo[m, n, i] 

		return dp(m, n, 0)
