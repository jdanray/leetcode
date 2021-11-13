# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/ 

class Solution(object):
	def removeOccurrences(self, s, part):
		M = len(s)
		N = len(part)

		for i, c in enumerate(s):
			j = i
			k = 0
			while j < M and k < N and s[j] == part[k]:
				j += 1
				k += 1

			if k >= N:
				return self.removeOccurrences(s[:i] + s[j:], part)

		return s
