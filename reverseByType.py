# https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/

class Solution(object):
	def reverseByType(self, s):
		abc = string.ascii_lowercase
		
		letters = []
		specials = []
		for c in s:
			if c in abc:
				letters.append(c)
			else:
				specials.append(c)

		res = ''
		for c in s:
			if c in abc:
				res += letters.pop()
			else:
				res += specials.pop()

		return res

"""
After I solve a problem, I like to study other people's solutions. It turns out that you can use a two-pointer technique to solve this problem:
"""

class Solution(object):
	def reverseByType(self, s):
		abc = string.ascii_lowercase

		letter = lambda c: c in abc
		special = lambda c: c not in abc

		s = list(s)

		def reverse(cond):
			i = 0
			j = len(s) - 1
			while i < j:
				if cond(s[i]) and cond(s[j]):
					s[i], s[j] = s[j], s[i]
					i += 1
					j -= 1
				elif cond(s[i]):
					j -= 1
				elif cond(s[j]):
					i += 1
				else:
					i += 1
					j -= 1

		reverse(letter)
		reverse(special)

		return ''.join(s)