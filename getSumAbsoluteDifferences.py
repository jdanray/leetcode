# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/ 

class Solution(object):
	def getSumAbsoluteDifferences(self, nums):
		N = len(nums)

		left = 0
		right = 0
		res = [0 for _ in range(N)]
		for i in range(N):
			if i > 0:
				left += i * (nums[i] - nums[i - 1])
				res[i] += left

			j = N - i - 1
			if j < N - 1:
				right += i * (nums[j + 1] - nums[j])
				res[j] += right

		return res

class Solution(object):
	def getSumAbsoluteDifferences(self, nums):
		N = len(nums)

		res = [0 for _ in range(N)]
		acc = 0
		for i in range(1, N):
			acc += i * (nums[i] - nums[i - 1])
			res[i] += acc

		acc = 0
		for i in range(N - 2, -1, -1):
			acc += (N - i - 1) * (nums[i + 1] - nums[i])
			res[i] += acc

		return res

class Solution(object):
	def getSumAbsoluteDifferences(self, nums):
		N = len(nums)

		left = [0 for _ in range(N)]
		for i in range(1, N):
			left[i] += left[i - 1]
			left[i] += i * (nums[i] - nums[i - 1])

		right = [0 for _ in range(N)]
		for i in range(N - 2, -1, -1):
			right[i] += right[i + 1]
			right[i] += (N - i - 1) * (nums[i + 1] - nums[i])

		return [left[i] + right[i] for i in range(N)]
