# https://leetcode.com/problems/longest-word-in-dictionary/

class Solution:
	def longestWord(self, words):
		longest = ""
		seen = set(words)
		for w in sorted(words):
			pre = ''
			i = 0
			while i < len(w):
				pre += w[i]
				if pre not in seen:
					break
				else:
					i += 1

			if i == len(w) and len(w) > len(longest):
				longest = w 

		return longest
