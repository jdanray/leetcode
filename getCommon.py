# https://leetcode.com/problems/minimum-common-value/ 

class Solution(object):
	def getCommon(self, nums1, nums2):
		c = set(nums1) & set(nums2)
		return min(c) if c else -1
