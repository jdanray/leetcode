# https://leetcode.com/problems/power-of-three/description/

class Solution:
	def isPowerOfThree(self, num):
		if num <= 0:
			return False
		f = 1
		while f < num:
			f *= 3
		return f == num
