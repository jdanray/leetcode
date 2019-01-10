# https://leetcode.com/problems/basic-calculator-ii/

class Solution(object):
	def calculate(self, s):
		values = []
		operators = []		
		i = 0

		# PEMDAS
		precedence = {}
		precedence['*'] = 2
		precedence['/'] = 2
		precedence['+'] = 1
		precedence['-'] = 1
		
		def operate(op, right, left):
			if op == '+':
				return left + right
			elif op == '-':
				return left - right
			elif op == '*':
				return left * right
			elif op == '/':
				return left // right
		
		while i < len(s):
			if s[i].isdigit():
				num = ''
				while i < len(s) and s[i].isdigit():
					num += s[i]
					i += 1
				values.append(int(num))
				i -= 1
			elif s[i] in {'+', '-', '*', '/'}:
				while operators and precedence[operators[-1]] >= precedence[s[i]]:
					values.append(operate(operators.pop(), values.pop(), values.pop()))
				operators.append(s[i])
			i += 1

		while operators:
			values.append(operate(operators.pop(), values.pop(), values.pop()))
		
		return values[-1]
