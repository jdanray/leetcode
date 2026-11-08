# https://leetcode.com/problems/find-mismatched-segments-between-two-strings/ 

class Solution(object):
	def findMismatchedSegments(self, s1, s2):
		N = len(s1)

		i = 0
		res = []
		while i < N:
			sub1 = ''
			sub2 = ''
			while i < N and s1[i] != s2[i]:
				sub1 += s1[i]
				sub2 += s2[i]
				i += 1

			if sub1:
				res.append([sub1, sub2])

			i += 1

		return res
