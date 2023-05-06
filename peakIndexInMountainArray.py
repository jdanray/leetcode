# https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution(object):
	def peakIndexInMountainArray(self, arr):
		def condition(value):
			return arr[value] > arr[value + 1]

		left = 1
		right = len(arr) - 2
		while left < right:
			mid = left + (right - left) // 2

			if condition(mid):
				right = mid
			else:
				left = mid + 1

		return left

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

class Solution(object):
	def peakIndexInMountainArray(self, A):
		i = 0
		while A[i] < A[i + 1]:
			i += 1
		return i
