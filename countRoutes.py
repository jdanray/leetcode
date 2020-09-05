# https://leetcode.com/problems/count-all-possible-routes/  

class Solution(object):
	def countRoutes(self, locations, start, finish, fuel):
		MOD = 10**9 + 7
		N = len(locations)

		memo = {}
		def dp(start, finish, fuel):
			if (start, finish, fuel) in memo:
				return memo[start, finish, fuel]
			elif (finish, start, fuel) in memo:
				return memo[finish, start, fuel]

			res = 0
			if start == finish:
				res = 1

			for mid in range(N):
				if mid == start: 
					continue

				dist = abs(locations[start] - locations[mid])
				if dist <= fuel:
					res += dp(mid, finish, fuel - dist)

			memo[start, finish, fuel] = res % MOD
			return memo[start, finish, fuel]

		return dp(start, finish, fuel) 
