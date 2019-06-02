# https://leetcode.com/problems/adding-two-negabinary-numbers/ 

class Solution(object):
	def toDec(self, nega):
		d = 0
		b = 1
		for n in nega[::-1]:
			d += n * b
			b *= (-2)
		return d

	def toNega(self, dec):
		if dec == 0:
			return [0]

		n = []
		dec = -dec
		while dec != 0:
			n = [dec & 1] + n
			dec //= (-2)
		return n

	def addNegabinary(self, arr1, arr2):
		s = self.toDec(arr1) + self.toDec(arr2)
		n = self.toNega(s)
		if n[0] == 0 and n != [0]:
			n = n[1:]
		return n
