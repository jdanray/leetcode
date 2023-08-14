# https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/ 

from sortedcontainers import SortedList

class Solution(object):
	def minAbsoluteDifference(self, nums, x):
		sl = SortedList()
		res = float('inf')
		for i, n in enumerate(nums):
			if i - x >= 0:
				sl.add(nums[i - x])
                
				j = bisect.bisect_left(sl, n)

				if j - 1 >= 0:
					res = min(res, n - sl[j - 1])

				if j < len(sl):
					res = min(res, sl[j] - n)

		return res
