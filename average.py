# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

class Solution(object):
	def average(self, salary):
		return float(sum(salary) - max(salary) - min(salary)) / (len(salary) - 2)
