# https://leetcode.com/problems/count-integers-appearing-in-a-single-block/ 

class Solution(object):
	def countSpecialIntegers(self, nums):
		seen = {}
		special = {n: True for n in nums}
		for i, n in enumerate(nums):
			if n not in seen or seen[n] == i - 1:
				seen[n] = i
			else:
				special[n] = False

		return sum(special.values())
