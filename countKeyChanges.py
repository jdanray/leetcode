# https://leetcode.com/problems/number-of-changing-keys/ 

class Solution(object):
	def countKeyChanges(self, s):
		return sum(s[i].upper() != s[i - 1] and s[i].lower() != s[i - 1] for i in range(1, len(s)))
