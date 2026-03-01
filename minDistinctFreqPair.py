# https://leetcode.com/problems/smallest-pair-with-different-frequencies/

class Solution(object):
	def minDistinctFreqPair(self, nums):
		freq = collections.Counter(nums)
		pair = [float('inf'), float('inf')]
		for x in nums:
			for y in nums:
				if x < y and freq[x] != freq[y]:
					pair = [min(pair[0], x), min(pair[1], y)]

		return [-1, -1] if pair == [float('inf'), float('inf')] else pair

class Solution(object):
	def minDistinctFreqPair(self, nums):
		freq = collections.Counter(nums)

		x = min(nums)
		y = float('inf')
		for n in freq:
			if freq[n] != freq[x]:
				y = min(y, n)

		return [-1, -1] if y == float('inf') else [x, y]

class Solution(object):
	def minDistinctFreqPair(self, nums):
		freq = collections.Counter(nums)

		x = min(nums)
		y = min([float('inf')] + [n for n in freq if freq[n] != freq[x]])

		return [-1, -1] if y == float('inf') else [x, y]