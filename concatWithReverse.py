# https://leetcode.com/problems/concatenate-array-with-reverse/

class Solution(object):
	def concatWithReverse(self, nums):
		return nums + nums[::-1]