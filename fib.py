# https://leetcode.com/problems/fibonacci-number/

class Solution(object):
	def fib(self, N):
		f = {}
		f[0] = 0
		f[1] = 1
		for n in range(2, N + 1):
			f[n] = f[n-1] + f[n-2]
		return f[N]
