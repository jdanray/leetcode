# https://leetcode.com/problems/count-elements-with-maximum-frequency/ 

class Solution(object):
	def maxFrequencyElements(self, nums):
		count = collections.Counter(nums)
		m = max(count.values())
		return sum(count[n] for n in count if count[n] == m)
