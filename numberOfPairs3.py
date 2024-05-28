# https://leetcode.com/problems/find-the-number-of-good-pairs-i/ 

class Solution(object):
	def numberOfPairs(self, nums1, nums2, k):
		return sum(n1 % (n2 * k) == 0 for n1 in nums1 for n2 in nums2)

class Solution(object):
	def numberOfPairs(self, nums1, nums2, k):
		res = 0
		for n1 in nums1:
			for n2 in nums2:
				if n1 % (n2 * k) == 0:
					res += 1
		return res
