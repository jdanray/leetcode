# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/ 

class Solution(object):
	def differenceOfSum(self, nums):
		elemSum = sum(nums)

		digSum = 0
		for n in nums:
			while n > 0:
				d = n % 10
				digSum += d
				n //= 10

		return abs(elemSum - digSum)
