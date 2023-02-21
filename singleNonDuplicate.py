# https://leetcode.com/problems/single-element-in-a-sorted-array/

class Solution(object):
	def singleNonDuplicate(self, nums):
		lo = 0
		hi = len(nums) - 1
		while lo < hi:
			mid = lo + (hi - lo) // 2
			if mid % 2 == 1:
				mid -= 1

			if nums[mid] == nums[mid + 1]:
				lo = mid + 2
			else:
				hi = mid

		return nums[lo]

class Solution(object):
	def singleNonDuplicate(self, nums):
		def condition(value):
			if value % 2 == 0:
				return nums[value] != nums[value + 1]
			else:
				return nums[value] != nums[value - 1]

		left = 0
		right = len(nums) - 1
		while left < right:
			mid = left + (right - left) // 2
            
			if condition(mid):
				right = mid
			else:
				left = mid + 1

		return nums[left]
