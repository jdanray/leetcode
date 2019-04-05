# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

class Solution(object):
	def findLongestWord(self, s, d):
		longest = ''
		for w in sorted(d):
			if len(w) < len(longest) or len(w) > len(s):
				continue

			i = 0
			for c in s:
				if i < len(w) and w[i] == c:
					i += 1

			if i == len(w) and len(w) > len(longest):
				longest = w

		return longest
