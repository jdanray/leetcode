# https://leetcode.com/problems/smallest-range-i/

class Solution:
	def smallestRangeI(self, A, K):
		return max(0, max(A) - min(A) - K * 2)
