# https://leetcode.com/problems/string-compression-iii/ 

class Solution(object):
	def compressedString(self, word):
		N = len(word)
		L = 9

		i = 0
		res = ''
		while i < N:
			c = word[i]
			l = 1
			i += 1

			while i < N and word[i] == c and l < L:
				l += 1
				i += 1

			res += str(l) + c 

		return res
