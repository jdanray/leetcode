# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

class Solution(object):
	def maxIncreasingSubarrays(self, nums):
		def condition(k):
			inc = [1 for _ in range(len(nums))]
			for i, n in enumerate(nums):
				if i - 1 >= 0 and n > nums[i - 1]:
					inc[i] = inc[i - 1] + 1

				if inc[i] >= k and i - k >= 0 and inc[i - k] >= k:
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

		return right