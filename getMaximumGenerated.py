# https://leetcode.com/problems/get-maximum-in-generated-array/

class Solution(object):
	def getMaximumGenerated(self, n):
		if n == 0 or n == 1:
			return n

		nums = [0 for _ in range(n + 1)]
		nums[0] = 0
		nums[1] = 1
		for i in range(2, n + 1):
			if i % 2 == 1:
				j = (i - 1) >> 1
				nums[i] = nums[j] + nums[j + 1]
			else:
				j = i >> 1
				nums[i] = nums[j]

		return max(nums)
