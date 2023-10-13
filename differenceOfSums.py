# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/ 

class Solution(object):
	def differenceOfSums(self, n, m):
		return sum(i * [1, -1][i % m == 0] for i in range(1, n + 1))

class Solution(object):
	def differenceOfSums(self, n, m):
		return sum(i * (-1 if i % m == 0 else 1) for i in range(1, n + 1))

class Solution(object):
	def differenceOfSums(self, n, m):
		num1 = 0
		num2 = 0
		for i in range(1, n + 1):
			if i % m != 0:
				num1 += i
			else:
				num2 += i

		return num1 - num2
