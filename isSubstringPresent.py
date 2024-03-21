# https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/ 

class Solution(object):
	def isSubstringPresent(self, s):
		rev = s[::-1]
		return any(s[i] + s[i + 1] in rev for i in range(len(s) - 1))
