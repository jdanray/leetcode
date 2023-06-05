# https://leetcode.com/problems/minimize-string-length/

class Solution(object):
	def minimizedStringLength(self, s):
		return len(set(s))
