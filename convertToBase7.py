# https://leetcode.com/problems/base-7/

class Solution:
	def convertToBase7(self, num):
		if num == 0:
			return "0"

		if num < 0:
			neg = True
			num = -num
		else:
			neg = False

		s = ""
		while num > 0:
			s = str(num % 7) + s
			num //= 7

		if neg:
			s = "-" + s

		return s

# After I solve a problem, I like to examine solutions that other people came up with. I found a really slick recursive solution and a way to streamline my own solution:

class Solution:
	def convertTo7(self, num):
		if num < 0: return '-' + self.convertTo7(-num)
		if num < 7: return str(num)
		return self.convertTo7(num // 7) + str(num % 7)

class Solution:
	def convertToBase7(self, num):
		if num == 0:
			return "0"

		n = abs(num)
		s = ""
		while n > 0:
			s = str(n % 7) + s
			n //= 7

		return ("-" if num < 0 else "") + s
