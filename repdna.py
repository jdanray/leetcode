# https://leetcode.com/problems/repeated-dna-sequences/description/

class Solution(object):
	def findRepeatedDnaSequences(self, s):
		l = 10
		seen = set()
		reps = set()
		for i in range(len(s) - l + 1):
			t = s[i:i + l]
			if t in seen:
				reps.add(t)
			else:
				seen.add(t)
		return list(reps)
