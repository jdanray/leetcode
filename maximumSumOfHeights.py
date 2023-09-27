# https://leetcode.com/problems/beautiful-towers-i/ 

"""
Idea: For each height, let it be the peak of the mountain. Move to the left, reducing each height as needed. Move to the right, reducing each height as needed. Take the sum of all the heights. Keep a running maximum for the sums. 

Invariant: res is the largest sum so far.
"""

class Solution(object):
	def maximumSumOfHeights(self, heights):
		res = 0
		for i, p in enumerate(heights):
			s = 0

			h = p
			for l in range(i, -1, -1):
				h = min(heights[l], h)
				s += h

			h = p
			for r in range(i + 1, len(heights)):
				h = min(heights[r], h)
				s += h

			res = max(res, s)

		return res
