# https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

class Solution(object):
	def reductionOperations(self, nums):
		nums = sorted(nums)
		smallest = nums[0]
		nextSmallest = nums[0]
		inc = 0
		res = 0
		for n in nums:
			if n > nextSmallest:
				smallest = nextSmallest
				nextSmallest = n
				inc += 1

			if n > smallest:
				res += inc

		return res

"""
After I solve a problem, I like to examine other people's solutions. I found a particularly elegant solution: 

https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/discuss/1253877/Sort-and-Count

Here is my Python implementation:
"""

class Solution(object):
	def reductionOperations(self, nums):
		N = len(nums)
		nums = sorted(nums)
		res = 0
		for i in range(N - 1, 0, -1):
			if nums[i] != nums[i - 1]:
				res += N - i

		return res
