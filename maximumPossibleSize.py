# https://leetcode.com/problems/make-array-non-decreasing/

class Solution(object):
	def maximumPossibleSize(self, nums):
		prev = float('-inf')
		i = 0
		res = 0
		while i < len(nums):
			while i < len(nums) and nums[i] < prev:
				i += 1

			if i < len(nums):
				prev = nums[i]
				i += 1
				res += 1

		return res

"""
After I solve problems, I like to study other people's solutions. I found a simpler solution here:

https://leetcode.com/problems/make-array-non-decreasing/solutions/6668653/do-we-really-need-operations-to-perform/

I will translate this Java solution into Python:
"""

class Solution(object):
	def maximumPossibleSize(self, nums):
		prev = float('-inf')
		res = 0
		for n in nums:
			if n >= prev:
				prev = n
				res += 1
                
		return res