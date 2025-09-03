# https://leetcode.com/problems/check-balanced-string/

class Solution(object):
	def isBalanced(self, num):
		return sum(int(num[i]) for i in range(0, len(num), 2)) == sum(int(num[i]) for i in range(1, len(num), 2))