# https://leetcode.com/problems/knight-dialer/

class Solution:
	def knightDialer(self, N):
		sup = 10 ** 9 + 7

		dest = {}
		dest[1] = [6, 8]
		dest[2] = [7, 9]
		dest[3] = [4, 8]
		dest[4] = [3, 9, 0]
		dest[5] = []
		dest[6] = [1, 7, 0]
		dest[7] = [2, 6]
		dest[8] = [1, 3]
		dest[9] = [2, 4]
		dest[0] = [4, 6]

		count = {n: 1 for n in range(10)}
		for _ in range(N - 1):
			newcount = {n: 0 for n in range(10)}
			for n in count:
				for d in dest[n]:
					newcount[d] += count[n]
			count = newcount

		return sum(count[n] for n in count) % sup
