# https://leetcode.com/problems/minimize-xor/

class Solution(object):
	def minimizeXor(self, num1, num2):
		nset = 0
		while num2 > 0:
			if num2 & 1 == 1:
				nset += 1
			num2 >>= 1

		p = 0
		n1 = num1
		ones = []
		while n1 > 0:
			if n1 & 1 == 1:
				ones.append(p)
			n1 >>= 1
			p += 1

		res = 0
		while ones and nset > 0:
			p = ones.pop()
			res += (2 ** p)
			nset -= 1

		n1 = num1
		p = 0
		while nset > 0:
			if n1 & 1 == 0:
				res += (2 ** p)
				nset -= 1
			p += 1
			n1 >>= 1

		return res 
