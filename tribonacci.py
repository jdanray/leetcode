# https://leetcode.com/problems/n-th-tribonacci-number/

class Solution(object):
	def tribonacci(self, n):
		t = {}
		t[0] = 0
		t[1] = 1
		t[2] = 1
		for i in range(3, n + 1):
			t[i] = t[i - 1] + t[i - 2] + t[i - 3]            
		return t[n]

class Solution(object):
	def tribonacci(self, n):
		t = [0, 1, 1]
		for _ in range(3, n + 1):
			t = [t[1], t[2], t[0] + t[1] + t[2]]

		return t[n] if n < len(t) else t[-1]
