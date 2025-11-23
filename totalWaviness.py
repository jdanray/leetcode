# https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/

class Solution(object):
	def totalWaviness(self, num1, num2):
		def waviness(num):
			l = m = r = -1
			res = 0
			while num > 0:
				l, m, r = m, r, num % 10

				num //= 10

				if l == -1 or m == -1 or r == -1:
					continue

				if (l < m and r < m) or (l > m and r > m):
					res += 1

			return res

		return sum(waviness(n) for n in range(num1, num2 + 1))

class Solution(object):
	def totalWaviness(self, num1, num2):
		res = 0
		for num in range(num1, num2 + 1):
			l = m = r = -1
			while num > 0:
				l, m, r = m, r, num % 10

				num //= 10

				if l == -1 or m == -1 or r == -1:
					continue

				if (l < m and r < m) or (l > m and r > m):
					res += 1

		return res