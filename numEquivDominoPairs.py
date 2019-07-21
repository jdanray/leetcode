# https://leetcode.com/problems/number-of-equivalent-domino-pairs/

class Solution(object):
	def numEquivDominoPairs(self, dominoes):
		n = 0
		freq = collections.defaultdict(int)
		for a, b in dominoes:
			if a > b:
				a, b = b, a
			n += freq[a, b]
			freq[a, b] += 1
		return n 
