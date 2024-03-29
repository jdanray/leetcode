# https://leetcode.com/problems/counting-bits/

class Solution:
	def countBits(self, num):
		if num == 0:
			return [0]
		elif num == 1:
			return [0, 1]

		B = [0, 1]
		m = 2
		newm = 4

		for n in range(2, num + 1):
			if n == newm:
				m = newm
				newm *= 2

			b = B[n % m] + 1
			B.append(b)

		return B

# After I solve a problem, I like to review other people's solutions
# The following is adapted from a solution on programcreek.com

class Solution:
	def countBits(self, num):
		B = [0]
		p = 0
		P = 2

		for n in range(1, num + 1):
			if n == P:
				P *= 2
				p = 0

			b = B[p] + 1
			B.append(b)

			p += 1

		return B

# I thought of a much simpler solution:

class Solution(object):
	def countBits(self, n):
		res = [0 for _ in range(n + 1)]
		for i in range(1, n + 1):
			res[i] = res[i // 2] + (i % 2)
		return res
