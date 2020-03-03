# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution(object):
	def evalRPN(self, tokens):
		operators = {}
		operators['+'] = lambda x, y: x + y
		operators['-'] = lambda x, y: x - y
		operators['*'] = lambda x, y: x * y
		operators['/'] = lambda x, y: int(float(x) / y)
        
		stack = []
		for t in tokens:
			if t in operators:
				op2 = stack.pop()
				op1 = stack.pop()
				res = operators[t](op1, op2)
				stack.append(res)
			else:
				stack.append(int(t))                
		return stack[-1]
