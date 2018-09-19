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
# This is adapted from a solution on programcreek.com
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
