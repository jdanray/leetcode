# https://leetcode.com/problems/construct-uniform-parity-array-i/ 

"""
You can always have a uniform array:

If nums1 is all evens or all odds, the array is already uniform.

If nums1 is neither all evens nor all odds, then nums1 has at least one even and at least one odd. You can construct an all-odds array by keeping the odds as-is and subtracting some odd from each even.
"""

class Solution(object):
	def uniformArray(self, nums1):
		return True
