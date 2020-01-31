# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/ 

class Solution(object):
	def minDominoRotations(self, A, B):
		INF = float('inf')
		N = len(A)
		AB = [A, B]

		def nflips(head, k):
			n = 0
			for i in range(N):
				if AB[k][i] == head:
					continue
				elif AB[1 - k][i] == head:
					n += 1
				else:
					return INF
			return n

		res = min(nflips(A[0], 0), nflips(A[0], 1), nflips(B[0], 0), nflips(B[0], 1))
		return res if res < INF else -1
