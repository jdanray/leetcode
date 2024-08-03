# https://leetcode.com/problems/find-if-digit-game-can-be-won/ 

class Solution(object):
	def canAliceWin(self, nums):
		return sum(n for n in nums if n < 10) != sum(n for n in nums if n >= 10)

class Solution(object):
	def canAliceWin(self, nums):
		single = 0
		double = 0
		for n in nums:
			if n < 10:
				single += n
			else:
				double += n

		return single != double
