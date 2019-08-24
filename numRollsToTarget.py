# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/ 

class Solution(object):
	def numRollsToTarget(self, d, f, target):
		MOD = (10 ** 9) + 7
		memo = collections.defaultdict(int)
		memo[0, 0] = 1
		for x in range(1, d + 1):
			for t in range(target + 1):
				if x > t: 
					continue
				for i in range(1, f + 1):
					memo[x, t] += memo[x - 1, t - i]
					memo[x, t] %= MOD
		return memo[d, target]
