# https://leetcode.com/problems/find-common-elements-between-two-arrays/ 

class Solution(object):
	def findIntersectionValues(self, nums1, nums2):
		res = [0, 0]

		for n1 in nums1:
			for n2 in nums2:
				if n1 == n2:
					res[0] += 1
					break

		for n2 in nums2:
			for n1 in nums1:
				if n1 == n2:
					res[1] += 1
					break

		return res
