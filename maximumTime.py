# https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/ 

class Solution(object):
	def maximumTime(self, time):
		res = ''
		for i, t in enumerate(time):
			if t != '?':
				res += t
			elif i == 0:
				if time[1] in '0123?':
					res += '2'
				else:
					res += '1'
			elif i == 1:
				if res[-1] == '2':
					res += '3'
				else:
					res += '9'
			elif i == 3:
				res += '5'
			elif i == 4:
				res += '9'

		return res	
