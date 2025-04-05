# https://leetcode.com/problems/sum-of-all-subset-xor-totals/ 

class Solution(object):
	def subsetXORSum(self, nums):
		def allxors(i, sub):
			if i >= len(nums):
				return sub
			else:
				return allxors(i + 1, sub) + allxors(i + 1, sub ^ nums[i])
		return allxors(0, 0)

class Solution(object):
	def subsetXORSum(self, nums):
		stack = [[0, 0]]
		res = 0
		while stack:
			x, i = stack.pop()

			if i >= len(nums):
				res += x
			else:
				stack.append([x ^ nums[i], i + 1])
				stack.append([x, i + 1])

		return res
