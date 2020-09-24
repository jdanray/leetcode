# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/ 

class Solution(object):
	def sumOddLengthSubarrays(self, arr):
		N = len(arr)
		res = 0
		for i in range(N):
			s = 0
			for j in range(i, N):
				s += arr[j]
				if (j - i) % 2 == 0:
					res += s
		return res
