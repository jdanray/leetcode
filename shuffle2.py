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
