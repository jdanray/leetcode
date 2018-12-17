# https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution(object):
	def peakIndexInMountainArray(self, A):
		i = 0
		while A[i] < A[i + 1]:
			i += 1
		return i
