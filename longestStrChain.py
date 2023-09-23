# https://leetcode.com/problems/longest-string-chain/ 

class Solution(object):
	def longestStrChain(self, words):
		words = sorted(words, key=len)

		def isPred(a, b):            
			if len(a) != len(b) - 1:
				return False
            
			i = 0
			for c in b:
				if i < len(a) and a[i] == c:
					i += 1
                    
			return i == len(b) - 1

		memo = {}
		def dp(i, prev):
			if i >= len(words):
				return 0

			if (i, prev) in memo:
				return memo[i, prev]

			res = dp(i + 1, prev) # leave
			if prev == -1 or isPred(words[prev], words[i]):
				res = max(res, 1 + dp(i + 1, i)) # take

			memo[i, prev] = res
			return memo[i, prev]

		return dp(0, -1)
