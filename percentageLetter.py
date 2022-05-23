# https://leetcode.com/problems/percentage-of-letter-in-string/ 

class Solution(object):
	def percentageLetter(self, s, letter):
		n = sum(c == letter for c in s)
		return int(math.floor(100 * float(n) / len(s)))
