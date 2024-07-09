# https://leetcode.com/problems/find-the-encrypted-string/ 

class Solution(object):
	def getEncryptedString(self, s, k):
		return ''.join(s[(i + k) % len(s)] for i, c in enumerate(s))

class Solution(object):
	def getEncryptedString(self, s, k):
		res = ''
		for i, c in enumerate(s):
			j = (i + k) % len(s)
			res += s[j]
		return res
