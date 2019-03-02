# https://leetcode.com/problems/repeated-string-match/

class Solution(object):
	def repeatedStringMatch(self, A, B):
		n = 0
		R = ''
		while len(R) < len(B):
			R += A
			n += 1

		if B in R:
			return n

		if B in R + A:
			return n + 1

		return -1

class Solution(object):
	def repeatedStringMatch(self, A, B, R='', n=0):
		if len(R) < len(B):
			return self.repeatedStringMatch(A, B, R + A, n + 1)
		elif B in R:
			return n
		elif B in R + A:
			return n + 1
		else:
			return -1

class Solution(object):
	def repeatedStringMatch(self, A, B, R='', n=0):
		if len(R) < len(B):
			return self.repeatedStringMatch(A, B, R + A, n + 1)

		if B in R:
			return n

		if B in R + A:
			return n + 1

		return -1
