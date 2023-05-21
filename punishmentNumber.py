# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

class Solution(object):
	def punishmentNumber(self, n):
		def isValid(i):
			stack = [[i * i, 0]]
			while stack:
				x, s = stack.pop()

				if x == 0 and s == i:
					return True

				p = 1
				while x > 0:
					d = x % 10
					s += (p * d)
					p *= 10
					x //= 10
					stack.append([x, s])

			return False

		return sum(i * i for i in range(1, n + 1) if isValid(i))
