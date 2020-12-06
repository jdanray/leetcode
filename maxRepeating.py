# https://leetcode.com/problems/maximum-repeating-substring/

class Solution(object):
	def maxRepeating(self, sequence, word):
		N = len(sequence)
		M = len(word)

		res = 0
		for i in range(N):
			k = 0
			while i < N and sequence[i:i + M] == word:
				k += 1
				i += M

			res = max(res, k)

		return res

"""
After I solve a problem, I like to examine other people's solutions. 

The leetcoder "lee215" found a solution that I liked so much I want to preserve it here. 

Link: https://leetcode.com/problems/maximum-repeating-substring/discuss/952026/JavaPython-3-Bruteforce-4-liners-./775531
"""

class Solution(object):
	def maxRepeating(self, s, w):
		return sum(w * i in s for i in xrange(1, 101))
