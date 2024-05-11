# https://leetcode.com/problems/reverse-pairs/ 

from sortedcontainers import SortedList

class Solution(object):
	def reversePairs(self, nums):
		sl = SortedList()
		res = 0
		for n in nums:
			res += len(sl) - sl.bisect_right(n * 2)
			sl.add(n)
		return res
