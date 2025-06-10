# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/

class Solution(object):
	def maxDifference(self, s):
		count = collections.Counter(s).values()
		maxOdd = max(c for c in count if c % 2 == 1)
		minEven = min(c for c in count if c % 2 == 0)
		return maxOdd - minEven