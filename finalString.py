# https://leetcode.com/problems/faulty-keyboard/ 

class Solution(object):
	def finalString(self, s):
		FAULTY = 'i'
		res = ''
		for c in s:
			if c == FAULTY:
				res = res[::-1]
			else:
				res += c
		return res
