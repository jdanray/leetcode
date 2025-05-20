# https://leetcode.com/problems/zero-array-transformation-ii/

class Solution(object):
	def minZeroArray(self, nums, queries):
		N = len(nums)

		def condition(k):
			dec = [0 for _ in range(N + 1)]
			for i in range(k):
				l, r, v = queries[i]
				dec[l] += v
				dec[r + 1] -= v

			for i in range(1, N):
				dec[i] += dec[i - 1]

			return all(dec[i] >= nums[i] for i in range(N))

		left, right = 0, len(queries)
		while left < right:
			mid = left + (right - left) // 2

			if condition(mid):
				right = mid
			else:
				left = mid + 1

		return left if condition(left) else -1