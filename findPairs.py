# https://leetcode.com/problems/k-diff-pairs-in-an-array/

class Solution:
	def findPairs(self, nums, k):
		count = collections.Counter(nums)
		npairs = 0
		for n in sorted(count):
			count[n] -= 1
			if n + k in count and count[n + k] > 0:
				npairs += 1
				count[n] -= 1
		return npairs
