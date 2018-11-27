# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
	def reverseWords(self, s):
		blank = ' '
		r = ''
		w = ''
		for c in s:
			if c == blank:
				r += w
				r += blank
				w = ''
			else:
				w = c + w
		return r + w
