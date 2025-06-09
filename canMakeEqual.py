# https://leetcode.com/problems/transform-array-to-all-equal-elements/

class Solution(object):
	def canMakeEqual(self, nums, k):
		def check(t, k):
			for i in range(len(nums)):
				if i == 0:
					n = nums[0]

				if n != t:
					if i + 1 >= len(nums) or k <= 0:
						return False
					else:
						n = -nums[i + 1]
						k -= 1
				elif i + 1 < len(nums):
					n = nums[i + 1]
			return True

		return check(1, k) or check(-1, k)