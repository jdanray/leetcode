# https://leetcode.com/problems/frequency-of-the-most-frequent-element/ 

# The problem doesn't require binary search. The sliding-window technique is sufficient.

class Solution(object):
	def maxFrequency(self, nums, k):
		nums = sorted(nums)
		d = 0
		i = 0
		res = 1
		for j in range(1, len(nums)):
			d += (j - i) * (nums[j] - nums[j - 1])

			while d > k:
				d -= (nums[j] - nums[i])
				i += 1

			res = max(res, j - i + 1)

		return res

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
