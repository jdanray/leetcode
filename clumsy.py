# https://leetcode.com/problems/clumsy-factorial/

class Solution(object):
	def clumsy(self, N):
		if N == 1:
			return 1

		if N == 2:
			return 2

		if N == 3:
			return 6

		if N >= 4:
			r = N * (N - 1) // (N - 2)
			r += (N - 3)
			N -= 4

		while N >= 4:
			r -= (N * (N - 1) // (N - 2))
			r += (N - 3)
			N -= 4

		if N == 3:
			r -= (N * (N - 1) // (N - 2))

		if N == 2:
			r -= (N * (N - 1))

		if N == 1:
			r -= N
		
		return r
