# https://leetcode.com/problems/minimum-operations-to-transform-array/

class Solution(object):
	def minOperations(self, nums1, nums2):
		last = float('inf')
		res = 0
		for i in range(len(nums1)):
			res += abs(nums1[i] - nums2[i])

			if nums1[i] <= nums2[-1] <= nums2[i] or nums1[i] >= nums2[-1] >= nums2[i]:
				last = 0

			last = min(last, abs(nums1[i] - nums2[-1]), abs(nums2[i] - nums2[-1]))

		return res + last + 1