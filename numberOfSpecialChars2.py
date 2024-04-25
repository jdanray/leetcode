# https://leetcode.com/problems/count-the-number-of-special-characters-ii/

class Solution(object):
	def numberOfSpecialChars(self, word):
		uppers = set()
		lowers = set()
		cands = set()
		excl = set()
		for c in word:
			if c.islower():
				if c in uppers:
					excl.add(c)
				else:
					lowers.add(c)
			elif c.lower() in lowers:
				cands.add(c.lower())
				uppers.add(c.lower())
			else:
				excl.add(c.lower())

		return sum(c in cands and c not in excl for c in string.ascii_lowercase)
