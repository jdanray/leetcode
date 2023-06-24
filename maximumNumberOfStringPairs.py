# https://leetcode.com/problems/find-maximum-number-of-string-pairs/ 

class Solution(object):
	def maximumNumberOfStringPairs(self, words):
		words = set(words)
		res = 0
		for w in words:
			r = w[::-1]
			if r in words and r != w:
				res += 1
                
		return res // 2
