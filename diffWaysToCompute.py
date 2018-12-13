# https://leetcode.com/problems/different-ways-to-add-parentheses/

class Solution(object):
	def diffWaysToCompute(self, expr):
		res = []
		for i in range(len(expr)):
			if expr[i] == '*' or expr[i] == '+' or expr[i] == '-':
				left = expr[:i]
				right = expr[i + 1:]
				for val1 in self.diffWaysToCompute(left):
					for val2 in self.diffWaysToCompute(right):
						if expr[i] == '*':
							res.append(val1 * val2)
						elif expr[i] == '-':
							res.append(val1 - val2)
						elif expr[i] == '+':
							res.append(val1 + val2)

		return res or [int(expr)]
