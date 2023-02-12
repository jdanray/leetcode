# https://leetcode.com/problems/find-the-array-concatenation-value/ 

class Solution(object):
	def findTheArrayConcVal(self, nums):
		def concat(a, b):
			c = b
			while c > 0:
				a *= 10
				c //= 10
			return a + b

		res = 0
		i = 0
		j = len(nums) - 1
		while i <= j:
			if i == j:
				res += nums[i]
			else:
				res += concat(nums[i], nums[j])
			i += 1
			j -= 1

		return res
