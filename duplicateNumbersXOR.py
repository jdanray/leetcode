# https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/ 

class Solution(object):
	def duplicateNumbersXOR(self, nums):
		seen = set()
		res = 0
		for n in nums:
			if n in seen:
				res ^= n
			seen.add(n)
		return res
