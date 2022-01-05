# https://leetcode.com/problems/jump-game/ 

class Solution(object):
	def canJump(self, nums):
		if len(nums) == 1:
			return True

		maxJump = 0
		for i, n in enumerate(nums):
			if n == 0 and maxJump <= i and i < len(nums) - 1:
				return False
			else:
				maxJump = max(maxJump, i + n)

		return True

"""
After I solve problems, I like to study other people's solutions. I found a simpler solution here:

https://leetcode.com/problems/jump-game/discuss/20917/Linear-and-simple-solution-in-C%2B%2B

I translated the C++ into un-Pythonic Python:
"""

class Solution(object):
	def canJump(self, nums):
		N = len(nums)

		maxJump = 0
		i = 0
		while i < N and i <= maxJump:
			maxJump = max(maxJump, i + nums[i])
			i += 1

		return i >= N
