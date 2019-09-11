# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
	def lengthOfLongestSubstring(self, s):
		seen = collections.defaultdict(bool)
		longest = 0
		i = 0
		j = 0
		while i < len(s) and j < len(s):
			if seen[s[j]]:
				seen[s[i]] = False
				i += 1
			else:
				seen[s[j]] = True
				j += 1
				longest = max(longest, j - i)
		return longest
