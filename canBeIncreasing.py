# https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/ 

class Solution(object):
	def canBeIncreasing(self, nums):
		N = len(nums)
		for i in range(N):
			seq = nums[:i] + nums[i + 1:]
			if all(seq[i - 1] < seq[i] for i in range(1, N - 1)):
				return True
            
		return False
