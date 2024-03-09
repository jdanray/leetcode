# https://leetcode.com/problems/minimum-common-value/ 

class Solution(object):
	def getCommon(self, nums1, nums2):
		i = 0
		j = 0
		while i < len(nums1) and j < len(nums2) and nums1[i] != nums2[j]:
			if nums1[i] > nums2[j]:
				j += 1
			else:
				i += 1

		return nums1[i] if i < len(nums1) and j < len(nums2) else -1

class Solution(object):
	def getCommon(self, nums1, nums2):
		nums1 = set(nums1)
		for n in nums2:
			if n in nums1:
				return n
		return -1

class Solution(object):
	def getCommon(self, nums1, nums2):
		c = set(nums1) & set(nums2)
		return min(c) if c else -1
