# https://leetcode.com/problems/number-of-pairs-satisfying-inequality/ 

from sortedcontainers import SortedList

class Solution(object):
	def numberOfPairs(self, nums1, nums2, diff):
		N = len(nums1)

		sl = SortedList()
		res = 0
		for j in range(N):
			res += sl.bisect_right(nums1[j] - nums2[j] + diff)
			sl.add(nums1[j] - nums2[j])

		return res
