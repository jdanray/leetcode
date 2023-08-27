# https://leetcode.com/problems/frog-jump/ 

class Solution(object):
	def canCross(self, stones):
		if stones[1] != 1:
			return False

		end = stones[-1]
		stones = set(stones)

		@functools.lru_cache(None)
		def dp(s, prev):
			#return s == end or any(k != 0 and s + k in stones and dp(s + k, k) for k in [prev, prev + 1, prev - 1])

			if s == end:
				return True

			for k in [prev, prev + 1, prev - 1]:
				s1 = s + k
				if k != 0 and s1 in stones and dp(s1, k):
					return True

			return False

		return dp(1, 1)
