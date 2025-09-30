# https://leetcode.com/problems/majority-frequency-characters/

class Solution(object):
	def majorityFrequencyGroup(self, s):
		g = collections.Counter(s)
		f = collections.Counter(g.values())
		m = max(f.values())
		mk = max(k for k in f if f[k] == m)

		return ''.join(c for c in g if g[c] == mk)