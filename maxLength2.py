# https://leetcode.com/problems/maximum-subarray-with-equal-products/

# Py3
class Solution(object):
	def maxLength(self, nums):
		res = 0
		for i in range(len(nums)):
			p = 1
			sub = []
			for j in range(i, len(nums)):
				p *= nums[j]
				sub.append(nums[j])

				if p == math.lcm(*sub) * math.gcd(*sub):
					res = max(res, j - i + 1)

		return res