# https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/ 

class Solution(object):
	def longestContinuousSubstring(self, s):
		alphabet = string.ascii_lowercase
		prev = {alphabet[i]: alphabet[i - 1] for i in range(1, len(alphabet))}

		res = 0
		sub = 0
		for i, c in enumerate(s):
			if c in prev and s[i - 1] == prev[c]:
				sub += 1
			else:
				sub = 1

			res = max(res, sub)

		return res
