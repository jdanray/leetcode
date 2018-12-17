# https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution(object):
	def peakIndexInMountainArray(self, A):
		i = 0
		while A[i] < A[i + 1]:
			i += 1
		return i

class Solution(object):
	def peakIndexInMountainArray(self, A):
		lo = 0
		hi = len(A) - 1
		while lo < hi:
			mid = lo + (hi - lo) // 2
			if A[mid - 1] > A[mid]:
				hi = mid
			elif A[mid] < A[mid + 1]:
				lo = mid
			else:
				return mid
