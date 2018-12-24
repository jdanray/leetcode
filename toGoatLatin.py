# https://leetcode.com/problems/goat-latin/description/

class Solution:
	def toGoatLatin(self, S):
		a = ''
		s = []
		vowels = {'a','e','i','o','u'}
		for w in S.split():
			a += 'a'
			if w[0].lower() not in vowels:
				w = w[1:] + w[0]
			w += 'ma'
			w += a
			s.append(w)
		return ' '.join(s)
