# https://leetcode.com/problems/number-of-valid-clock-times/ 

class Solution(object):
	def countTime(self, time):
		res = 1

		if time[0] == '?':
			if time[1] in '0123?':
				res *= 3
			else:
				res *= 2

		if time[1] == '?':
			if time[0] == '?':
				res *= 8
			elif time[0] == '2':
				res *= 4
			else:
				res *= 10

		if time[3] == '?':
			res *= 6

		if time[4] == '?':
			res *= 10

		return res
