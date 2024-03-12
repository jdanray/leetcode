# https://leetcode.com/problems/apple-redistribution-into-boxes/ 

class Solution(object):
	def minimumBoxes(self, apple, capacity):
		capacity = sorted(capacity, reverse=True)
		s = sum(apple)
		i = 0
		while s > 0:
			s -= capacity[i]
			i += 1
		return i
