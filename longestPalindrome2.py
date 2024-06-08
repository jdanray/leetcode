# https://leetcode.com/problems/longest-palindrome/ 

class Solution(object):
	def longestPalindrome(self, s):
		count = collections.Counter(s)
		return sum((count[c] // 2) * 2 for c in count) + any(count[c] % 2 == 1 for c in count)

class Solution(object):
	def longestPalindrome(self, s):
		count = collections.Counter(s)
		res = 0
		for c in count:
			res += (count[c] // 2) * 2
			if res % 2 == 0 and count[c] % 2 == 1:
				res += 1
		return res
