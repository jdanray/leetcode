# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

class Solution(object):
	def removeDuplicates(self, s, k):
		if not s:
			return ""

		r = 1
		for i in range(1, len(s)):
			if s[i] == s[i - 1]:
				r += 1
			else:
				r = 1

			if r == k:
				return self.removeDuplicates(s[:i - r + 1] + s[i + 1:], k)

		return s
