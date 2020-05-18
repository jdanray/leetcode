# https://leetcode.com/problems/decompress-run-length-encoded-list/

class Solution(object):
	def decompressRLElist(self, nums):
		res = []
		for i in range(0, len(nums), 2):
			res += [nums[i + 1]] * nums[i]
		return res 
