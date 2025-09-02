# https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/submissions/

class Solution(object):
	def isPossibleToRearrange(self, s, t, k):
		h = len(s) // k
		scount = collections.Counter()
		tcount = collections.Counter()
		for i in range(0, len(s), h):
			scount[s[i:i + h]] += 1
			tcount[t[i:i + h]] += 1

		return scount == tcount