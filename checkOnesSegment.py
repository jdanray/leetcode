# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/ 

class Solution(object):
	def checkOnesSegment(self, s):
		seen = -1
		for i, b in enumerate(s):
			if b == '1':
				if seen == -1 or seen == i - 1:
					seen = i
				else:
					return False
		return True
