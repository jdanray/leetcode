# https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/

class Solution(object):
	def minDeletion(self, s, k):
		count = sorted(collections.Counter(s).values())
		return sum(count[i] for i in range(max(0, len(count) - k)))