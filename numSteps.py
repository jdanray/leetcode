# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/ 

class Solution(object):
	def numSteps(self, s):
		def str2int(s):
			num = 0
			d = 1
			for c in s[::-1]:
				if c == '1':
					num += d
				d <<= 1
			return num

		num = str2int(s)
		res = 0
		while num != 1:
			if num % 2 == 1:
				num += 1
			else:
				num //= 2
			res += 1
		return res

class Solution(object):
	def numSteps(self, s):
		carry = False
		res = 0
		for i in range(len(s) - 1, -1, -1):
			if s[i] == '0':
				if carry:
					res += 2	# treat as '1': add 1, divide by 2
				else:
					res += 1
			elif i != 0 or carry:
				if carry:
					res += 1
				else:
					carry = True
					res += 2

		return res
