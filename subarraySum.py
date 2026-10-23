# https://leetcode.com/problems/sum-of-variable-length-subarrays/


class Solution(object):
	def subarraySum(self, nums):
		N = len(nums)

		sums = [0 for _ in range(N)]
		res = 0
		for i in range(N):
			sums[i] += nums[i]
			if i > 0:
				sums[i] += sums[i - 1]

			res += sums[i]
			if i - nums[i] > 0:
				res -= sums[i - nums[i] - 1]

		return res

class Solution(object):
	def subarraySum(self, nums):
		N = len(nums)

		sums = [0 for _ in range(N)]
		res = 0
		for i in range(N):
			if i == 0:
				sums[i] = nums[i]
			else:
				sums[i] += sums[i - 1] + nums[i]

			if i - nums[i] <= 0:
				res += sums[i]
			else:
				res += sums[i] - sums[i - nums[i] - 1]

		return res

class Solution(object):
	def subarraySum(self, nums):
		N = len(nums)

		sums = [0 for _ in range(N)]
		for i in range(N):
			if i == 0:
				sums[i] = nums[i]
			else:
				sums[i] += sums[i - 1] + nums[i]

		res = 0
		for i in range(N):
			if i - nums[i] <= 0:
				res += sums[i]
			else:
				res += sums[i] - sums[i - nums[i] - 1]

		return res