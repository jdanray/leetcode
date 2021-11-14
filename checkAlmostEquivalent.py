# https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/ 

class Solution(object):
	def checkAlmostEquivalent(self, word1, word2):
		LIMIT = 3

		freq1 = collections.Counter(word1)
		freq2 = collections.Counter(word2)

		return all(abs(freq1[c] - freq2[c]) <= LIMIT for c in string.ascii_lowercase)
