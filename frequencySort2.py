# https://leetcode.com/problems/sort-array-by-increasing-frequency/ 

class Solution(object):
	def frequencySort(self, nums):
		freq = collections.Counter(nums)
		return sorted(nums, key=lambda n: (freq[n], -n))
