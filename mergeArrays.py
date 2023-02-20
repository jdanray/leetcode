# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/ 

class Solution(object):
	def mergeArrays(self, nums1, nums2):
		M = 1000

		sums = collections.defaultdict(int)

		for (i, v) in nums1:
			sums[i] += v

		for (i, v) in nums2:
			sums[i] += v

		return [[i, sums[i]] for i in range(1, M + 1) if sums[i] > 0]
