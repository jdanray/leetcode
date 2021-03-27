# https://leetcode.com/problems/second-largest-digit-in-a-string/ 

class Solution(object):
	def secondHighest(self, s):
		dig = set(c for c in s if c.isdigit())
		return sorted(dig)[-2] if len(dig) > 1 else -1
