# https://leetcode.com/problems/solve-the-equation/

class Solution(object):
	def parse(self, symbols):
		n = ""
		nums = 0
		xs = 0
		for s in symbols:
			if s == 'x':
				if not n or n == '+':
					n = 1
				elif n == '-':
					n = -1

				xs += int(n)
				n = ""
				continue

			if n and (s == '-' or s == '+'):
				nums += int(n)
				n = ""
			n += s

		if n:
			nums += int(n)

		return xs, nums

	def solveEquation(self, equation):
		lhs, rhs = equation.split("=")

		lxs, lnums = self.parse(lhs)
		rxs, rnums = self.parse(rhs)

		xs = lxs - rxs
		nums = rnums - lnums

		if xs == 0:
			if nums == 0:
				return "Infinite solutions"
			else:
				return "No solution"
		else:
			return "x=" + str(nums // xs)
