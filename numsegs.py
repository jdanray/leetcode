# https://leetcode.com/problems/number-of-segments-in-a-string/

class Solution(object):
	def countSegments(self, s):
		seg = False
		count = 0
		for c in s:
			if c == ' ':
				seg = False
			elif seg == False:
				seg = True
				count += 1
		return count
