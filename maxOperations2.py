# https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i/ 

class Solution(object):
	def maxOperations(self, nums):
		score = nums[0] + nums[1]
		res = 1
		for i in range(0, len(nums), 2):
			if i + 1 >= len(nums) or nums[i] + nums[i + 1] != score:
				break
			else:
				res += 1
		return res
