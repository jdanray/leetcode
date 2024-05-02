# https://leetcode.com/problems/find-the-integer-added-to-array-i/ 

class Solution(object):
	def addedInteger(self, nums1, nums2):
		return min(nums2) - min(nums1)
