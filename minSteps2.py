# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/ 

class Solution(object):
	def minSteps(self, s, t):
		counts = collections.Counter(s)
		countt = collections.Counter(t)

		ds = sum(max(0, counts[c] - countt[c]) for c in counts) 
		dt = sum(max(0, countt[c] - counts[c]) for c in countt)

		return ds + dt
