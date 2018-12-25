# https://leetcode.com/problems/merge-sorted-array/

class Solution(object):
	def merge(self, nums1, m, nums2, n):
		i = m - 1
		j = n - 1
		l = m + n - 1
		while i >= 0 and j >= 0:
			if nums1[i] > nums2[j]:
				nums1[l] = nums1[i]
				i -= 1
			else:
				nums1[l] = nums2[j]
				j -= 1
			l -= 1

		while j >= 0:
			nums1[l] = nums2[j]
			j -= 1
			l -= 1
