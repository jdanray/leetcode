# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/ 

class Solution(object):
	def countTriplets(self, arr):
		N = len(arr)

		res = 0
		for i in range(N):
			a = 0 
			for j in range(i, N):
				a ^= arr[j]
				b = 0
				for k in range(j + 1, N):
					b ^= arr[k]
					if a == b:
						res += 1

		return res
