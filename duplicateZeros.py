# https://leetcode.com/problems/duplicate-zeros/

class Solution(object):
	def duplicateZeros(self, arr):
		N = len(arr)
		i = 0
		while i < N:
			if arr[i] != 0 or N <= i + 1:
				i += 1
				continue

			j = N - 1
			while j > i:
				arr[j] = arr[j - 1]
				j -= 1

			arr[i + 1] = 0
			i += 2
