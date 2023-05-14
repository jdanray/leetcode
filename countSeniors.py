# https://leetcode.com/problems/number-of-senior-citizens/ 

class Solution(object):
	def countSeniors(self, details):
		A = 11
		S = 60

		res = 0
		for p in details:
			if int(p[A] + p[A + 1]) > S:
				res += 1

		return res
