# https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/

class Solution(object):
	def kthLargestValue(self, matrix, k):
		M = len(matrix)
		N = len(matrix[0])

		cands = []
		val = [0 for _ in range(N)]		# val[j] == value of coord (i - 1, j), for fixed i and any j
		for i in range(M):
			xor = 0				# xor = matrix[i][0] ^ matrix[i][1] ^ ... ^ matrix[i][j - 1]
			for j in range(N):
				xor ^= matrix[i][j]	# update for the current j 
				val[j] ^= xor		# value(i, j) == value(i - 1, j) ^ xor
				cands.append(val[j])	# remember all values we encounter

		cands = sorted(cands, reverse=True)
		return cands[k - 1]
