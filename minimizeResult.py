# https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/ 

class Solution(object):
	def minimizeResult(self, expr):
		def myInt(c):
			return int(c) if c else 1
 
		p = expr.find('+')
		minProd = float('inf')
		res = ''
		for i in range(p):
			for j in range(p + 2, len(expr) + 1):
				adLeft = expr[i:p]
				adRight = expr[p + 1:j] 
				muLeft = expr[:i]
				muRight = expr[j:]

				prod = myInt(muLeft) * (int(adLeft) + int(adRight)) * myInt(muRight)
				
				if prod < minProd:
					minProd = prod
					res = muLeft + '(' + adLeft + '+' + adRight + ')' + muRight

		return res
