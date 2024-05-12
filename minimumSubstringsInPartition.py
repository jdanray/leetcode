# https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/ 

class Solution(object):
	def minimumSubstringsInPartition(self, s):
		@functools.lru_cache(None)
		def dp(i):
			if i >= len(s):
				return 0

			count = collections.Counter()
			res = float('inf')
			for j in range(i, len(s)):
				count[s[j]] += 1
				if all(count[c] == count[s[j]] for c in count):
					res = min(res, 1 + dp(j + 1)) 

			return res

		return dp(0)
