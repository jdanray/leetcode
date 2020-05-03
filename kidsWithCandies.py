# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution(object):
	def kidsWithCandies(self, candies, extraCandies):
		return [c + extraCandies >= max(candies) for c in candies]
