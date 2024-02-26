# https://leetcode.com/problems/split-the-array/ 

class Solution(object):
	def isPossibleToSplit(self, nums):
		count = collections.Counter(nums)
		return all(count[n] <= 2 for n in count)
