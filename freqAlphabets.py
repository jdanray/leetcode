# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

class Solution(object):
	def freqAlphabets(self, s):
		alphabet = 'abcdefghijklmnopqrstuvwxyz'
		num2char = {}
		for i, c in enumerate(alphabet):
			if i + 1 > 9:
				num = str(i + 1) + '#'
			else:
				num = str(i + 1)
                
			num2char[num] = c

		N = len(s)
		res = ''
		i = 0
		while i < N:
			if i + 2 < N and s[i + 2] == '#':
				num = s[i:i + 3]
				i += 3
			else:
				num = s[i]
				i += 1

			res += num2char[num]

		return res
