# https://leetcode.com/problems/maximum-points-in-an-archery-competition/ 

class Solution(object):
	def maximumBobPoints(self, numArrows, aliceArrows):
		N = len(aliceArrows)

		def solve(i, soln, free, score):
			if i >= N:
				return score, soln, free

			noshoot = solve(i + 1, soln, free, score)
			if free > aliceArrows[i]:
				shoot = solve(i + 1, soln + (1 << i), free - aliceArrows[i] - 1, score + i)
				return shoot if shoot[0] > noshoot[0] else noshoot
			else:
				return noshoot 

		_, soln, free = solve(1, 0, numArrows, 0)
		res = [0 for _ in range(N)]
		res[0] = free
		for i in range(N):
			if (soln >> i) & 1 == 1:
				res[i] = aliceArrows[i] + 1

		return res
