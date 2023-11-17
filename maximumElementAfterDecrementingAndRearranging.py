# https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/ 

class Solution(object):
	def maximumElementAfterDecrementingAndRearranging(self, arr):
		arr = sorted(arr)
		arr[0] = 1
		for i in range(1, len(arr)):
			if arr[i] - arr[i - 1] > 1:
				arr[i] = arr[i - 1] + 1

		return max(arr)

class Solution(object):
	def maximumElementAfterDecrementingAndRearranging(self, arr):
		arr = sorted(arr)
		arr[0] = 1
		prev = 1
		res = 1
		for a in arr:
			if a - prev > 1:
				prev += 1
			else:
				prev = a
                
			res = max(res, prev)

		return res
