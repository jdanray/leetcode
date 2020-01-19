# https://leetcode.com/problems/maximum-69-number/

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
