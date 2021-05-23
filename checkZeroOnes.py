# https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/ 

class Solution(object):
	def checkZeroOnes(self, s):
		maxOnes = 0
		maxZeros = 0
		ones = 0
		zeros = 0
		for i, c in enumerate(s):
			if c == '1':
				if i == 0 or s[i - 1] != '1':
					ones = 1
				else:
					ones += 1
			elif c == '0':
				if i == 0 or s[i - 1] != '0':
					zeros = 1
				else:
					zeros += 1

			maxOnes = max(maxOnes, ones)
			maxZeros = max(maxZeros, zeros)

		return maxOnes > maxZeros
