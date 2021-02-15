# https://leetcode.com/problems/sum-of-unique-elements/

class Solution(object):
	def sumOfUnique(self, nums):
		count = collections.Counter(nums)
		return sum([n for n in nums if count[n] == 1])
