# https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

class Solution(object):
	def minSum(self, nums1, nums2):
		s1 = sum(1 if n == 0 else n for n in nums1)
		s2 = sum(1 if n == 0 else n for n in nums2)

		if s1 == s2:
			return s1
		elif s1 > s2:
			return s1 if 0 in nums2 else -1
		elif s2 > s1:
			return s2 if 0 in nums1 else -1

