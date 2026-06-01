# https://leetcode.com/problems/digit-frequency-score/

class Solution(object):
	def digitFrequencyScore(self, n):
		s = 0
		while n > 0:
			s += n % 10
			n //= 10
		return s