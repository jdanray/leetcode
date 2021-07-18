# https://leetcode.com/problems/maximum-number-of-words-you-can-type/

class Solution(object):
	def canBeTypedWords(self, text, brokenLetters):
		broken = set(brokenLetters)
		words = text.split()
		res = 0
		for w in words:
			if all(c not in broken for c in w):
				res += 1
		return res
