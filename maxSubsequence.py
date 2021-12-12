# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/ 

class Solution(object):
	def maxSubsequence(self, nums, k):
		res = zip(nums, range(len(nums)))
		res = sorted(res)
		res = res[-k:]
		res = sorted(res, key=lambda r: r[1])
		return [r[0] for r in res]
