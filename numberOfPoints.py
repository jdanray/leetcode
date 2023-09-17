# https://leetcode.com/problems/points-that-intersect-with-cars/

class Solution(object):
	def numberOfPoints(self, nums):
		seen = set()
		for (s, e) in nums:
			for n in range(s, e + 1):
				seen.add(n)
                
		return len(seen)
