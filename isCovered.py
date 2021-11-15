# https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/ 

class Solution(object):
	def isCovered(self, ranges, left, right):
		#covered = {x for (start, end) in ranges for x in range(start, end + 1)}

		covered = set()
		for (start, end) in ranges:
			for x in range(start, end + 1):
				covered.add(x)

		return all(x in covered for x in range(left, right + 1))
