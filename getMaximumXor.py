# https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution(object):
	def getMaximumXor(self, nums, maximumBit):
		N = len(nums)
		maxK = 1 << maximumBit

		xor = nums[0]
		for i in range(1, N):
			xor ^= nums[i]

		res = [0 for _ in range(N)]
		for i in range(N):
			k = 0
			for j in range(maximumBit - 1, -1, -1):
				if (xor >> j) & 1 == 0 and k + (1 << j) < maxK:
					k += (1 << j)

			res[i] = k
			xor ^= nums[N - i - 1]

		return res
