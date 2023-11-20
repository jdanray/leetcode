# https://leetcode.com/problems/separate-black-and-white-balls/ 

class Solution(object):
	def minimumSteps(self, s):
		z = 0
		res = 0
		for i, b in enumerate(s):
			if b == '0':
				res += i - z
				z += 1
		return res
