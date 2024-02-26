# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/ 

class Solution(object):
	def longestCommonPrefix(self, arr1, arr2):
		prefixes = set()
		for a in arr1:
			p = ''
			for c in str(a):
				p += c
				prefixes.add(p)

		lcp = ''
		for a in arr2:
			p = ''
			for c in str(a):
				p += c
				if p in prefixes and len(p) > len(lcp):
					lcp = p

		return len(lcp)
