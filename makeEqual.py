# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/  

class Solution(object):
	def makeEqual(self, words):
		count = collections.Counter(c for w in words for c in w)
		return all(count[c] % len(words) == 0 for c in count)
