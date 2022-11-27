# https://leetcode.com/problems/minimum-penalty-for-a-shop/ 

class Solution(object):
	def bestClosingTime(self, customers):
		penalty = customers.count('Y')
		minPenalty = penalty
		res = 0
		for i, c in enumerate(customers):
			if c == 'Y':
				penalty -= 1
			else:
				penalty += 1

			if penalty < minPenalty:
				res = i + 1
				minPenalty = penalty

		return res
