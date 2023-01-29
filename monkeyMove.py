# https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/ 

class Solution(object):
	def monkeyMove(self, n):
		MOD = 10**9 + 7

		if n == 3:
			return 6

		if n % 2 == 1 or n == 4:
			return (2 * self.monkeyMove(n - 1) + 2) % MOD

		res = self.monkeyMove(n // 2)
		return (res * (res + 4) + 2) % MOD
