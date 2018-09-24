# https://leetcode.com/problems/custom-sort-string/description/

class Solution:
	def customSortString(self, S, T):
		chars = 'abcdefghijklmnopqrstuvwxyz'
		freq = {c: 0 for c in chars}
		for c in T:
			freq[c] += 1

		U = ''
		for c in S:
			while freq[c] > 0:
				U += c
				freq[c] -= 1

		for c in freq:
			while freq[c] > 0:
				U += c
				freq[c] -= 1

		return U
