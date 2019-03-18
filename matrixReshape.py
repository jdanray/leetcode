# https://leetcode.com/problems/reshape-the-matrix/

class Solution:
	def matrixReshape(self, nums, r, c):
		h = len(nums)
		w = len(nums[0])
		if h * w != r * c:
			return nums

		res = [[-1 for _ in range(c)] for _ in range(r)]
		k = 0
		l = 0
		for i in range(h):
			for j in range(w):
				if l >= c:
					k += 1
					l = 0
				res[k][l] = nums[i][j]
				l += 1

		return res
