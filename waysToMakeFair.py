# https://leetcode.com/problems/ways-to-make-a-fair-array/ 

class Solution(object):
	def waysToMakeFair(self, nums):
		N = len(nums)

		right = [[0, 0] for _ in range(N)]
		for i in range(N - 1, 0, -1):
			right[i - 1] = [right[i][0], right[i][1]]
			right[i - 1][i % 2 == 0] += nums[i]

		left = [0, 0]
		res = 0
		for i in range(N):
			if left[0] + right[i][0] == left[1] + right[i][1]:
				res += 1
			left[i % 2 != 0] += nums[i]

		return res
