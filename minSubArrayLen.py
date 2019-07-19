# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution(object):
	def minSubArrayLen(self, s, nums):
		def window(mid):
			c = 0
			for i, n in enumerate(nums):
				c += n
				if i >= mid: 
					c -= nums[i - mid]
				if c >= s: 
					return True
			return False

		m = 0
		lo = 1
		hi = len(nums)
		while lo <= hi:
			mid = lo + (hi - lo) // 2
			if window(mid):
				hi = mid - 1
				m = mid
			else:
				lo = mid + 1
		return m
