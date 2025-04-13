# https://leetcode.com/problems/smallest-palindromic-rearrangement-i/

class Solution(object):
	def smallestPalindrome(self, s):
		count = collections.Counter(s)
		i = 0
		j = len(s) - 1
		res = [''] * len(s)
		for c in string.ascii_lowercase:
			while count[c] > 1:
				res[i] = c
				res[j] = c

				count[c] -= 2
				i += 1
				j -= 1

		for c in string.ascii_lowercase:
			if count[c] == 1:
				res[i] = c
				i += 1

		return ''.join(res)