# https://leetcode.com/problems/detect-capital/description/

class Solution(object):
	def detectCapitalUse(self, word):
		lowercase = set('abcdefghijklmnopqrstuvwxyz')
		uppercase = set(c.upper() for c in lowercase)
		for i in range(len(word) - 1):
			if word[i] in lowercase and word[i + 1] in uppercase:
				return False
			elif word[i] in uppercase and word[i + 1] in lowercase and i != 0:
				return False
		return True

class Solution:
	def detectCapitalUse(self, word):
		if all(word[i] == word[i].lower() for i in range(len(word))):
			return True
		elif all(word[i] == word[i].upper() for i in range(len(word))):
			return True
		elif word[0] == word[0].upper() and all(word[i] == word[i].lower() for i in range(len(word))):
			return True
		else:
			return False
