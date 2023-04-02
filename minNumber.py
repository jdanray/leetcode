# https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/ 

class Solution(object):
	def minNumber(self, nums1, nums2):
		for n in range(1, 10):
			if n in nums1 and n in nums2:
				return n

		m1 = min(nums1)
		m2 = min(nums2)
		if m1 < m2:
			return 10 * m1 + m2
		else:
			return 10 * m2 + m1
