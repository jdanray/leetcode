# https://leetcode.com/problems/palindrome-partitioning/ 

class Solution(object):
	def isPalindrome(self, p):
		i = 0
		j = len(p) - 1
		while i < j:
			if p[i] != p[j]:
				return False
			i += 1
			j -= 1
		return True

	def helper(self, s, start, part):
		if start >= len(s):
			self.res.append(part)
			return True

		p = ''
		for i in range(start, len(s)):
			p += s[i]
			if self.isPalindrome(p):
				self.helper(s, i + 1, part + [p])

	def partition(self, s):
		self.res = []
		self.helper(s, 0, [])
		return self.res
