# https://leetcode.com/problems/min-max-game/ 

class Solution(object):
	def minMaxGame(self, nums):
		while len(nums) > 1:
			newNums = [0 for _ in range(len(nums) // 2)]
			takeMin = True
			for i in range(0, len(nums), 2):
				if takeMin:
					newNums[i // 2] = min(nums[i], nums[i + 1])
				else:
					newNums[i // 2] = max(nums[i], nums[i + 1])
			
				takeMin = not takeMin

			nums = newNums

		return nums[0]
