# https://leetcode.com/problems/longest-balanced-substring-i/

class Solution(object):
	def longestBalanced(self, s):
		res = 0
		for i in range(len(s)):
			count = collections.Counter()
			for j in range(i, -1, -1):
				count[s[j]] += 1

				if all(count[c] == count[s[j]] for c in count):
					res = max(res, i - j + 1)

		return res