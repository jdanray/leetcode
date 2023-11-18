# https://leetcode.com/problems/frequency-of-the-most-frequent-element/ 

class Solution(object):
	def maxFrequency(self, nums, k):
		nums = sorted(nums)

		def condition(value):
			if value == 1:
				return True

			d = 0
			for i in range(1, len(nums)):
				if i >= value:
					d -= (nums[i - 1] - nums[i - value])

				d += min(i, value - 1) * (nums[i] - nums[i - 1])

				if i >= value - 1 and d <= k:
					return True

			return False

		left = 1
		right = len(nums)
		while left <= right:
			mid = left + (right - left) // 2

			if condition(mid):
				left = mid + 1
			else:
				right = mid - 1

		return left - 1
