# https://leetcode.com/problems/to-lower-case/ 

class Solution(object):
	def toLowerCase(self, string):
		upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		lower = 'abcdefghijklmnopqrstuvwxyz'
		tolower = {upper[i]: lower[i] for i in range(len(upper))}
		low = ''
		for c in string:
			if c in tolower:
				low += tolower[c]
			else:
				low += c
		return low
