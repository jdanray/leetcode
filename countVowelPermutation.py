# https://leetcode.com/problems/count-vowels-permutation/

class Solution(object):
	def countVowelPermutation(self, n):
		MOD = 10**9 + 7
		vowels = "aeiou"

		prev = {}
		prev['a'] = 'eiu'
		prev['e'] = 'ai'
		prev['i'] = 'eo'
		prev['o'] = 'i'
		prev['u'] = 'io'

		dp = collections.defaultdict(int)
		for v in vowels: 
			dp[1, v] = 1

		for i in range(2, n + 1):
			for v in vowels:
				for p in prev[v]:
					dp[i, v] += dp[i - 1, p]

		return sum(dp[n, v] for v in vowels) % MOD 
