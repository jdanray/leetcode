# https://leetcode.com/problems/max-chunks-to-make-sorted/

from sortedcontainers import SortedList

class Solution(object):
	def maxChunksToSorted(self, arr):
		seen = SortedList()
		target = 0
		res = 0
		for n in arr:
			seen.add(n)            
			if len(seen) == seen[-1] - target + 1:
				target = seen[-1] + 1
				seen.clear()
				res += 1

		return res