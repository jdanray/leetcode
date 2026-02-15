# https://leetcode.com/problems/number-of-prefix-connected-groups/

class Solution(object):
	def prefixConnected(self, words, k):
		count = collections.Counter(w[:k] for w in words if len(w) >= k)
		return len([v for v in count.values() if v >= 2])