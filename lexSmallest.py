# https://leetcode.com/problems/lexicographically-smallest-string-after-reverse/

class Solution(object):
	def lexSmallest(self, s):
		res = s
		for k in range(len(s)):
			a = s[:k]
			b = s[k:]
			res = min(res, a[::-1] + b, a + b[::-1])
		return res