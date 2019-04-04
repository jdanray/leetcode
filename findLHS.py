# https://leetcode.com/problems/longest-harmonious-subsequence/

from collections import Counter

class Solution:
	def findLHS(self, nums):
		m = 0
		count = Counter(nums)
		keys = sorted(count)
		for i in range(1, len(keys)):
			if keys[i] - keys[i - 1] == 1:
				m = max(m, count[keys[i]] + count[keys[i - 1]])
		return m

"""
After I solve a problem, I like to look at other people's solutions
The following solution is simpler and faster, and the code is prettier
"""

class Solution:
	def findLHS(self, nums):
		m = 0
		count = Counter(nums)
		for n in count:
			if n + 1 in count:
				m = max(m, count[n] + count[n + 1])
		return m
