# https://leetcode.com/problems/minimum-operations-to-make-a-special-number/ 

class Solution(object):
	def minimumOperations(self, num):
		N = len(num)
		f = -1
		z = -1
		res = N
		for i in range(N - 1, -1, -1):
			if num[i] == '5' and f == -1:
				f = i
			if num[i] == '0' and z == -1:
				z = i
				res = min(res, N - 1)

			if num[i] in '27' and f != -1:
				res = min(res, (N - f - 1) + (f - i - 1))
			if num[i] in '05' and z != -1 and z != i:
				res = min(res, (N - z - 1) + (z - i - 1))

		return res
