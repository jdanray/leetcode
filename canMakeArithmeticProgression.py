# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/ 

class Solution(object):
	def canMakeArithmeticProgression(self, arr):
		arr = sorted(arr)
		return all(arr[i] - arr[i - 1] == arr[i - 1] - arr[i - 2] for i in range(2, len(arr)))
