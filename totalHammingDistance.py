# https://leetcode.com/problems/total-hamming-distance/ 

class Solution(object):
	def totalHammingDistance(self, nums):
		N = 32        
		diff = {i: [0, 0] for i in range(N)}
		for n in nums:
			for i in range(N):
				diff[i][n & 1] += 1
				n >>= 1

		return sum(diff[i][0] * diff[i][1] for i in range(N))
