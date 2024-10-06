# https://leetcode.com/problems/sentence-similarity-iii/ 

class Solution(object):
	def areSentencesSimilar(self, sentence1, sentence2):
		s1 = sentence1.split()
		s2 = sentence2.split()

		if len(s1) == len(s2):
			return s1 == s2

		# ensure that s2 is longer than s1
		if len(s1) > len(s2):
			s1, s2 = s2, s1

		# suffix
		# add sentence to end of s1
		# s2 = s1 + sentence

		if s1 == s2[:len(s1)]:
			return True

		# prefix
		# add sentence to beginning of s1
		# s2 = sentence + s1

		if s1 == s2[-len(s1):]:
			return True

		# infix
		# add sentence to middle of s1
		# s2 = s1[:i] + sentence + s1[i:]

		i = 0
		j = 0
		while i < len(s1) and s1[i] == s2[j]:
			i += 1
			j += 1

		k = len(s1) - 1
		l = len(s2) - 1
		while k >= i and s1[k] == s2[l]:
			k -= 1
			l -= 1

		return k < i
