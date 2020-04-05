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
