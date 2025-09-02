# https://leetcode.com/problems/find-special-substring-of-length-k/

class Solution(object):
	def hasSpecialSubstring(self, s, k):
		count = 0
		for i, c in enumerate(s):
			if i - 1 >= 0 and s[i - 1] == c:
				count += 1
			else:
				count = 1

			if count == k and (i - k < 0 or s[i - k] != c) and (i + 1 >= len(s) or s[i + 1] != c):
				return True

		return False