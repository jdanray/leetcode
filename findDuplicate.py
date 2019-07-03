# https://leetcode.com/problems/find-the-duplicate-number/

class Solution(object):
	def findDuplicate(self, nums):
		lo = 0
		hi = len(nums) - 1
		while lo < hi:
			mid = lo + (hi - lo) // 2

			count = 0
			for n in nums:
				if n <= mid:
					count += 1

			if count > mid:
				hi = mid
			else:
				lo = mid + 1

		return hi
