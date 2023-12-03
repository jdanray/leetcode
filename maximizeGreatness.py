# https://leetcode.com/problems/maximize-greatness-of-an-array/ 

from sortedcontainers import SortedList

class Solution(object):
	def maximizeGreatness(self, nums):
		sl = SortedList(nums)
		res = 0
		for n in nums:
			i = sl.bisect_right(n)
			if i < len(sl) and sl[i] > n:
				res += 1
				sl.remove(sl[i])
			else:
				sl.remove(sl[0])

		return res
