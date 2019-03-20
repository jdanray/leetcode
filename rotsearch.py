# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
	def search(self, nums, target):
		left = 0
		right = len(nums) - 1
		while left < right:
			mid = left + (right - left) // 2
			if nums[mid] < nums[right]:
				right = mid
			else:
				left = mid + 1
		
		shift = left
		left = 0
		right = len(nums) - 1
		while left <= right:
			mid = left + (right - left) // 2
			shiftmid = (mid + shift) % len(nums)
			if nums[shiftmid] == target:
				return shiftmid
			elif target > nums[shiftmid]:
				left = mid + 1
			else:
				right = mid - 1

		return -1
