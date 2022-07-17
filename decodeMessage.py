# https://leetcode.com/problems/decode-the-message/ 

class Solution(object):
	def decodeMessage(self, key, message):
		n = 0
		sub = {}
		for c in key:
			if c.isalpha() and c not in sub:
				sub[c] = string.ascii_lowercase[n]
				n += 1

		return ''.join(sub[c] if c in sub else c for c in message) 
