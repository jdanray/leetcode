# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/ 

class Solution(object):
	def countPalindromicSubsequence(self, s):
		N = len(s)

		res = 0
		for p in string.ascii_lowercase:
			start = 0
			while start < N and s[start] != p:
				start += 1

			seen = set()
			used = set()
			for i in range(start + 1, N):
				if s[i] == p:
					for c in seen:
						if c not in used:
							res += 1
							used.add(c)
					seen = set()

				seen.add(s[i])

		return res
