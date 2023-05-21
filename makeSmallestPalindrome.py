# https://leetcode.com/problems/lexicographically-smallest-palindrome/ 

class Solution(object):
	def makeSmallestPalindrome(self, s):
		N = len(s)

		i = 0
		j = N - 1
		res = ['' for _ in range(N)]
		while i <= j:
			res[i] = min(s[i], s[j])
			res[j] = min(s[i], s[j])

			i += 1
			j -= 1

		return ''.join(res)
