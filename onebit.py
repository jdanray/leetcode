# https://leetcode.com/problems/1-bit-and-2-bit-characters/description/

class Solution(object):
	def isOneBitCharacter(self, bits):
		last = -1
		i = 0
		while i < len(bits):
			last = bits[i]
			if bits[i] == 1:
				i += 2
			elif bits[i] == 0:
				i += 1
		return last == 0
