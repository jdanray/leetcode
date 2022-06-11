# https://leetcode.com/problems/match-substring-after-replacement/ 

class Solution(object):
	def matchReplacement(self, s, sub, mappings):
		N = len(s)
		M = len(sub)

		alt = collections.defaultdict(set)
		for (old, new) in mappings:
			alt[old].add(new)

		for i in range(N):
			j = i
			k = 0
			while j < N and k < M and (s[j] == sub[k] or s[j] in alt[sub[k]]):
				j += 1
				k += 1

			if k >= M:
				return True

		return False
