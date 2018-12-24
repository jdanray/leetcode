# https://leetcode.com/problems/reverse-only-letters/

class Solution(object):
	def reverseOnlyLetters(self, S):
		S = list(S)
		i = 0
		j = len(S) - 1
		while i < j:
			if not S[i].isalpha():
				i += 1
			elif not S[j].isalpha():
				j -= 1
			else:
				S[i], S[j] = S[j], S[i]
				i += 1
				j -= 1
		return ''.join(S)	
