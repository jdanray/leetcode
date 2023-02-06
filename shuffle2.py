# https://leetcode.com/problems/shuffle-the-array/

class Solution(object):
	def shuffle(self, nums, n):
		N = len(nums)

		res = [0 for _ in range(N)]
		k = 0
		for i in range(N):
			if i == n:
				k = 1

			res[k] = nums[i]
			k += 2

		return res

class Solution(object):
	def shuffle(self, nums, n):
		res = [0] * (2 * n)
		for i in range(n):
			res[2 * i] = nums[i]
			res[2 * i + 1] = nums[n + i]

		return res
