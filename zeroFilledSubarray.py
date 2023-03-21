# https://leetcode.com/problems/number-of-zero-filled-subarrays/ 

class Solution(object):
	def zeroFilledSubarray(self, nums):
		res = 0
		i = 0
		for j, n in enumerate(nums):
			if n == 0:
				if j == 0 or nums[j - 1] != 0:
					i = j
				res += (j - i + 1)
		return res

class Solution(object):
	def zeroFilledSubarray(self, nums):
		i = 0
		res = 0
		for j, n in enumerate(nums):
			if n == 0:
				res += j - i + 1
			else:
				i = j + 1
		return res
