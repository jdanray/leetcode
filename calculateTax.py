# https://leetcode.com/problems/calculate-amount-paid-in-taxes/ 

class Solution(object):
	def calculateTax(self, brackets, income):
		i = 0
		prev = 0
		res = 0
		total = 0
		while total < income:
			amt = min(income, brackets[i][0]) - prev

			res += amt * (brackets[i][1] / 100.0)
 
			total += amt
			prev = brackets[i][0]
			i += 1

		return res
