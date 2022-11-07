# https://leetcode.com/problems/maximum-69-number/

class Solution(object):
	def maximum69Number(self, num):
		n = str(num)
		for i, d in enumerate(n):
			if d == '6':
				return int(n[:i] + '9' + n[i + 1:])

		return num 

class Solution(object):
	def maximum69Number(self, num):
		num = str(num)
		res = ''
		noflip = True
		for n in num:
			if n == '6' and noflip:
				res += '9'
				noflip = False
			else:
				res += n
                
		return int(res)
