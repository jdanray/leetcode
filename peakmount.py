# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

class Solution(object):
	def peakIndexInMountainArray(self, A):
		i = 1
		while i < len(A) and A[i] > A[i - 1]:
			i += 1
		return i
