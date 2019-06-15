# https://leetcode.com/problems/replace-words/

class Solution(object):
	def replaceWords(self, dict, sentence):
		dict = set(dict)
		words = sentence.split()
		for i, w in enumerate(words):
			r = ''
			for letter in w:
				r += letter
				if r in dict:
					words[i] = r
					break

		return ' '.join(words)
