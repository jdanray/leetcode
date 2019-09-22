# https://leetcode.com/problems/longest-mountain-in-array/

class Solution(object):
	def longestMountain(self, A):
		res = 0
		start = 0
		up = False
		for i in range(1, len(A)):
			if A[i] > A[i - 1]:
				if i - 2 >= 0 and A[i - 1] <= A[i - 2]:
					start = i - 1
				up = True
			elif A[i] < A[i - 1]:
				if up:
					res = max(res, i - start + 1)
			else:
				up = False                
		return res
