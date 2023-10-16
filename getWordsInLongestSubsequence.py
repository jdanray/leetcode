# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/ 

class Solution(object):
	def getWordsInLongestSubsequence(self, n, words, groups):
		prev = -1
		res = []
		for i, w in enumerate(words):
			if prev == -1 or groups[prev] != groups[i]:
				prev = i
				res.append(w)

		return res
