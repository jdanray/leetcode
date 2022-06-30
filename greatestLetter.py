# https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/

class Solution(object):
	def greatestLetter(self, s):
		lower = string.ascii_lowercase
		upper = string.ascii_uppercase

		seen = set(s)
		for i in range(len(upper) - 1, -1, -1):
			if lower[i] in seen and upper[i] in seen:
				return upper[i]

		return ''
