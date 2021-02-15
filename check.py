# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

class Solution(object):
	def check(self, arr):
		N = len(arr)

		i = 1
		while i < N and arr[i - 1] <= arr[i]:
			i += 1

		if i == N:
			return True

		if arr[i] > arr[0]:
			return False

		i += 1
		while i < N and arr[i - 1] <= arr[i] and arr[i] <= arr[0]:
			i += 1

		return i == N
