# https://leetcode.com/problems/day-of-the-week/ 

import datetime

class Solution(object):
	def dayOfTheWeek(self, day, month, year):
		return datetime.datetime(year, month, day).strftime("%A")

