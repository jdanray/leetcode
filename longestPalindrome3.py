# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

class Solution(object):
	def longestPalindrome(self, words):
		count = collections.Counter(words)
		odd = 0
		res = 0
		for l in count:
			r = l[1] + l[0]
			if l == r:
				if count[l] % 2 == 1:
					odd = 1
				res += 2 * (count[l] // 2)
			else:
				res += min(count[l], count[r])

		return 2 * (res + odd)

class Solution(object):
	def longestPalindrome(self, words):
		count = collections.Counter(words)
		return 2 * (sum(2 * (count[l] // 2) if l == l[1] + l[0] else min(count[l], count[l[1] + l[0]]) for l in count) + any(count[l] % 2 for l in count if l == l[1] + l[0]))