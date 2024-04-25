# https://leetcode.com/problems/longest-ideal-subsequence/ 

class Solution(object):
	def longestIdealString(self, s, k):
		alphabet = string.ascii_lowercase
		char2num = {c: n for n, c in enumerate(alphabet)}

		dp = collections.defaultdict(int)
		res = 0
		for c in s:
			n = char2num[c]

			for i in range(n - k, n + k + 1):
				dp[n] = max(dp[n], dp[i])

			dp[n] += 1
			res = max(res, dp[n])

		return res

class Solution(object):
	def longestIdealString(self, s, k):
		dp = {c: 0 for c in string.ascii_lowercase}
		for c in s:
			dp[c] = max(dp[c], max(1 + dp[x] for x in string.ascii_lowercase if abs(ord(c) - ord(x)) <= k))

		return max(dp.values())
