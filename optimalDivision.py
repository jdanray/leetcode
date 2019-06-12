# https://leetcode.com/problems/optimal-division/

class Solution:
	def optimalDivision(self, nums):
		if not nums:
			return ''
		elif len(nums) == 1:
			return str(nums[0])
		elif len(nums) == 2:
			return '%i/%i' % (nums[0], nums[1])
		else:
			return '%i/(%s)' % (nums[0], '/'.join(str(nums[i]) for i in range(1, len(nums))))
