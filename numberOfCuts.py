# https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/

class Solution(object):
	def numberOfCuts(self, n):
		if n == 1:
			return 0
		elif n % 2 == 0:
			return n // 2
		else:
			return n
