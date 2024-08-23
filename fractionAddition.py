# https://leetcode.com/problems/fraction-addition-and-subtraction/ 

class Solution(object):
	def fractionAddition(self, expr):
		numers = []
		denoms = []
		i = 0
		while i < len(expr):
			sign = 1
			if expr[i] == '-':
				sign = -1
				i += 1
			elif expr[i] == '+':
				i += 1

			n = ''
			while expr[i] != '/':
				n += expr[i]
				i += 1

			i += 1
			d = ''
			while i < len(expr) and expr[i] != '+' and expr[i] != '-':
				d += expr[i]
				i += 1

			numers.append(int(n) * sign)
			denoms.append(int(d))

		l = math.lcm(*denoms)
		s = sum(n * l // denoms[i] for i, n in enumerate(numers))
		g = math.gcd(s, l)

		return str(s // g) + '/' + str(l // g)
