# https://leetcode.com/problems/semi-ordered-permutation/

class Solution(object):
	def semiOrderedPermutation(self, nums):
		N = len(nums)
		i = nums.index(1)
		j = nums.index(N)
        
		return i + N - j - 1 - (j < i)

class Solution(object):
	def semiOrderedPermutation(self, nums):
		N = len(nums)

		i = nums.index(1)

		j = nums.index(N)
		if j < i:
			j += 1

		return i + N - j - 1
