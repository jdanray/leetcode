# https://leetcode.com/problems/number-of-employees-who-met-the-target/ 

class Solution(object):
	def numberOfEmployeesWhoMetTarget(self, hours, target):
		return len([h for h in hours if h >= target])
