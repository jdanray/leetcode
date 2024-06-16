# https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/ 

class Solution(object):
	def countCompleteDayPairs(self, hours):
		M = 24
		res = 0
		for j, h in enumerate(hours):
			for i in range(j):
				if (hours[i] + h) % M == 0:
					res += 1
		return res

class Solution(object):
	def countCompleteDayPairs(self, hours):
		M = 24
		return sum((hours[i] + h) % M == 0 for j, h in enumerate(hours) for i in range(j))
