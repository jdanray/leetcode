# https://leetcode.com/problems/reverse-prefix-of-word/ 

class Solution(object):
	def reversePrefix(self, word, ch):
		for i, w in enumerate(word):
			if w == ch:
				return word[:i + 1][::-1] + word[i + 1:]

		return word
