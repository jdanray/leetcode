# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

class Solution(object):
	def longestSubsequence(self, arr, difference):
		long = collections.defaultdict(int)
		for num in arr:
			long[num] = max(long[num], long[num - difference] + 1)
		return max(long.values())
