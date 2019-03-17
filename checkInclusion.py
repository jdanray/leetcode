# https://leetcode.com/problems/permutation-in-string/

from collections import Counter

class Solution:
	def checkInclusion(self, s1, s2):
		if len(s2) < len(s2):
			return []

		s1count = Counter(s1)
		s2count = Counter(s2[:len(s1) - 1])

		for i in range(len(s2) - len(s1) + 1):
			s2count[s2[i + len(s1) - 1]] += 1

			if s1count == s2count:
				return True

			s2count[s2[i]] -= 1
			if s2count[s2[i]] == 0:
				del s2count[s2[i]]

		return False
