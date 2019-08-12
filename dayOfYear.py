# https://leetcode.com/problems/ordinal-number-of-date/

class Solution(object):
	def dayOfYear(self, date):
		ndays = [31,28,31,30,31,30,31,31,30,31,30,31]
		year, month, day = map(int, date.split('-'))
		leap = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) 
		res = 0
		for m in range(month - 1):
			res += ndays[m]
			if leap and m == 1: 
				res += 1
		res += day
		return res
