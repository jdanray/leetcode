# https://leetcode.com/problems/string-to-integer-atoi/

class Solution(object):
	def myAtoi(self, string):
		nums = {str(n) for n in range(10)}
		INTMIN = -2 ** 31
		INTMAX = 2 ** 31 - 1
		N = len(string)

		i = 0
		while i < N and string[i] == ' ':
			i += 1
            
		if i >= N:
			return 0

		neg = False
		digs = []
		if string[i] == '-': 
			neg = True
		elif string[i] in nums:
			digs = [int(string[i])] + digs
		elif string[i] != '+':
			return 0
        
		i += 1
		while i < N and string[i] in nums:
			digs = [int(string[i])] + digs
			i += 1

		res = 0
		b = 1
		for d in digs:
			res += d * b
			b *= 10
            
		if neg:
			res = -res

		if res < INTMIN:
			return INTMIN
		elif res > INTMAX:
			return INTMAX
		else:
			return res 
