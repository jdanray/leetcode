# https://leetcode.com/problems/palindrome-partitioning/ 

class Solution(object):
	def partition(self, s):
		def isPalindrome(p):
			i = 0
			j = len(p) - 1
			while i < j:
				if p[i] != p[j]:
					return False
				i += 1
				j -= 1
			return True

		def doPartition(start, part):
			if start >= len(s):
				res.append(part)
				return True

			p = ''
			for i in range(start, len(s)):
				p += s[i]
				if isPalindrome(p):
					doPartition(i + 1, part + [p])

		res = []
		doPartition(0, [])
		return res
