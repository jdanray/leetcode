# https://leetcode.com/problems/count-distinct-numbers-on-board/

class Solution(object):
	def distinctIntegers(self, n):
		return n - 1 if n > 1 else n
