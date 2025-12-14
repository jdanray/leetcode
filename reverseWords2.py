# https://leetcode.com/problems/reverse-words-with-same-vowel-count/

class Solution(object):
	def reverseWords(self, s):
		def vowelCount(w):
			vowels = 'aeiou'
			res = 0
			for c in w:
				if c in vowels:
					res += 1
			return res

		words = s.split()
		v0 = vowelCount(words[0])
		for i in range(1, len(words)):
			if vowelCount(words[i]) == v0:
				words[i] = words[i][::-1]

		return ' '.join(words)