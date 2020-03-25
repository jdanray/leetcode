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

class Solution(object):
	def lengthOfLongestSubstring(self, s):
		count = collections.defaultdict(int)
		j = 0
		res = 0
		for i, c in enumerate(s):
			count[c] += 1
			while count[c] > 1:
				count[s[j]] -= 1
				j += 1
			res = max(res, i - j + 1)
		return res 
