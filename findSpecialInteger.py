# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

class Solution(object):
	def findSpecialInteger(self, arr):
		k = len(arr) // 4
		for i in range(len(arr)):
			if arr[i] == arr[i + k]:
				return arr[i]
