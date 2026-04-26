# https://leetcode.com/problems/valid-elements-in-an-array/

class Solution(object):
	def findValidElements(self, nums):
		elems = []
		for i, n in enumerate(nums):
			if all(nums[j] < n for j in range(i)):
				elems.append(n)
			elif all(nums[j] < n for j in range(i + 1, len(nums))):
				elems.append(n)

		return elems