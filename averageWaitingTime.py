# https://leetcode.com/problems/average-waiting-time/ 

class Solution(object):
	def averageWaitingTime(self, customers):
		start = 1
		wait = 0.0
		for (a, p) in customers:
			start = max(start, a)
			end = start + p
			wait += (end - a)
			start = end
		return wait / len(customers)
