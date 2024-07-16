# https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/ 

class Solution(object):
	def getSmallestString(self, s):
		for i in range(len(s) - 1):
			if int(s[i]) % 2 == int(s[i + 1]) % 2 and int(s[i]) > int(s[i + 1]):
				return s[:i] + s[i + 1] + s[i] + s[i + 2:]
		return s
