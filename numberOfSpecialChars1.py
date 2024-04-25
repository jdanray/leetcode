# https://leetcode.com/problems/count-the-number-of-special-characters-i/ 

class Solution(object):
	def numberOfSpecialChars(self, word):
		seen = [set(), set()]
		for c in word:
			seen[c.isupper()].add(c.lower())

		return sum(c in seen[0] and c in seen[1] for c in string.ascii_lowercase) 
