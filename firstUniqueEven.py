# https://leetcode.com/problems/first-unique-even-element/

class Solution(object):
	def firstUniqueEven(self, nums):
		count = collections.Counter(nums)

		for n in nums:
			if n % 2 == 0 and count[n] == 1:
				return n

		return -1