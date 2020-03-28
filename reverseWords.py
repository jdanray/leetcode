# https://leetcode.com/problems/reverse-words-in-a-string/ 

class Solution(object):
	def reverseWords(self, s):
		return ' '.join(w for w in reversed(s.split()))

class Solution(object):
	def reverseWords(self, s):
		words = s.split()
		i = 0
		j = len(words) - 1
		while i < j:
			words[i], words[j] = words[j], words[i]
			i += 1
			j -= 1
		return ' '.join(words)
