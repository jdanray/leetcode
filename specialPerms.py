# https://leetcode.com/problems/special-permutations/ 

class Solution(object):
	def specialPerm(self, nums):
		N = len(nums)
		MOD = 10**9 + 7

		memo = {}
		def dp(prev, used):
			if used == (1 << N) - 1:
				return 1

			if (prev, used) in memo:
				return memo[prev, used]

			res = 0
			for i, n in enumerate(nums):
				if (used >> i) & 1 == 0 and (prev == None or n % prev == 0 or prev % n == 0):
					res += dp(n, used | (1 << i))

			memo[prev, used] = res
			return memo[prev, used]

		return dp(None, 0) % MOD
