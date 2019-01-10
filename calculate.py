class Solution(object):
	def calculate(self, s):
		values = []
		operators = []		
		i = 0
		
		def operate(op, right, left):
			if op == '+':
				return left + right
			elif op == '-':
				return left - right
		
		while i < len(s):
			if s[i].isdigit():
				num = ''
				while i < len(s) and s[i].isdigit():
					num += s[i]
					i += 1
				values.append(int(num))
				i -= 1
			elif s[i] in {'+', '-'}:
				while operators and operators[-1] != '(':
					values.append(operate(operators.pop(), values.pop(), values.pop()))
				operators.append(s[i])
			elif s[i] == '(':
				operators.append(s[i])
			elif s[i] == ')':
				while operators[-1] != '(':
					values.append(operate(operators.pop(), values.pop(), values.pop()))
				operators.pop()
			
			i += 1

		while operators:
			values.append(operate(operators.pop(), values.pop(), values.pop()))
		
		return values[-1]
