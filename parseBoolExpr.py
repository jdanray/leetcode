# https://leetcode.com/problems/parsing-a-boolean-expression/

class Solution(object):
	def parseBoolExpr(self, expression):
		def exprend(i):
			k = i + 2
			open = 1
			while open != 0:
				if expression[k] == '(':
					open += 1
				elif expression[k] == ')':
					open -= 1
				k += 1
			return k

		def conjun(i, j):
			while i <= j:
				if expression[i] == 'f':
					return False

				if expression[i] == 't' or expression[i] == ',':
					i += 1
					continue

				k = exprend(i)
				if not parse(i, k - 1):
					return False

				i = k + 1

			return True

		def altern(i, j):
			while i <= j:
				if expression[i] == 't':
					return True

				if expression[i] == 'f' or expression[i] == ',':
					i += 1
					continue

				k = exprend(i)
				if parse(i, k - 1):
					return True

				i = k + 1

			return False

		def parse(i, j):
			if expression[i] == 't':
				return True

			if expression[i] == 'f':
				return False

			if expression[i] == '!':
				return not parse(i + 2, j - 1)

			if expression[i] == '&':
				return conjun(i + 2, j - 1)

			if expression[i] == '|':
				return altern(i + 2, j - 1)

		return parse(0, len(expression) - 1)
