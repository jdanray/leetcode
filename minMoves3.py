# https://leetcode.com/problems/minimum-moves-to-balance-circular-array/

class Solution(object):
	def minMoves(self, balance):
		N = len(balance)

		n = -1
		s = 0
		for i, b in enumerate(balance):
			if b < 0:
				n = i
			else:
				s += b

		if n == -1:
			return 0

		if s < -balance[n]:
			return -1

		d = 1
		res = 0
		while balance[n] < 0:
			l = (n - d) % N
			r = (n + d) % N

			for i in [l, r]:
				c = min(balance[i], -balance[n])
				balance[n] += c
				res += d * c

			d += 1

		return res