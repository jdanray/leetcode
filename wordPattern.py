# https://leetcode.com/problems/word-pattern/description/

class Solution(object):
	def wordPattern(self, pattern, string):
		words = string.split()
		if len(words) != len(pattern):
			return False

		pd = dict()
		wd = dict()
		for i in range(len(words)):
			if words[i] not in wd:
				wd[words[i]] = pattern[i]
			if pattern[i] not in pd:
				pd[pattern[i]] = words[i]

			if wd[words[i]] != pattern[i]:
				return False
			if pd[pattern[i]] != words[i]:
				return False
		return True
