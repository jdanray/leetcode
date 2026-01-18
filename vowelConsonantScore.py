# https://leetcode.com/problems/vowel-consonant-score/

class Solution(object):
	def vowelConsonantScore(self, s):
		vowels = 'aeiou'

		v = 0.0
		c = 0.0
		for x in s:
			if x in vowels:
				v += 1
			elif x != ' ' and not x.isdigit():
				c += 1

		return int(math.floor(v / c)) if c > 0 else 0