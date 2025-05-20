# https://leetcode.com/problems/zero-array-transformation-i/

class Solution(object):
	def isZeroArray(self, nums, queries):
		N = len(nums)

		dec = [0 for _ in range(N + 1)]
		for (l, r) in queries:
			dec[l] += 1
			dec[r + 1] -= 1

		for i in range(1, N):
			dec[i] += dec[i - 1]

		return all(dec[i] >= nums[i] for i in range(N))