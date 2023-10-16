# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/ 

"""
The algorithm is a modification of the standard algorithm that solves the longest increasing subsequence problem. 

Imports technique from Dijkstra's algorithm to keep track of longest paths.
"""
class Solution(object):
	def getWordsInLongestSubsequence(self, n, words, groups):
		def hammingDist(w1, w2):
			# assume that len(w1) == len(w2)
			return sum(w1[i] != w2[i] for i in range(len(w1)))

		def isAcceptable(i, j):
			return len(words[i]) == len(words[j]) and groups[i] != groups[j] and hammingDist(words[i], words[j]) == 1

		# dp[i][1] is the length of the longest subsequence that ends with words[i]
		# dp[i][0] is the index of the element of the subsequence immediately previous to words[i]
		dp = [[-1, 1] for i in range(n)]

		# maxim[1] is the length of the longest subsequence overall
		# maxim[0] is the index of the final element in the subsequence
		maxim = [0, 1]

		for i in range(1, len(words)):
			for j in range(i):
				if isAcceptable(j, i) and dp[i][1] < dp[j][1] + 1:
					dp[i] = [j, dp[j][1] + 1]
					if maxim[1] < dp[j][1] + 1:
						maxim = [i, dp[j][1] + 1]

		idx = maxim[0]
		res = [words[idx]]
		while dp[idx][0] != -1:
			idx = dp[idx][0]
			res.append(words[idx])

		return res[::-1]
