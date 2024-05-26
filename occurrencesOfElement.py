# https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/ 

class Solution(object):
	def occurrencesOfElement(self, nums, queries, x):
		occ = [i for i, n in enumerate(nums) if n == x]
		return [occ[q - 1] if q <= len(occ) else -1 for q in queries]
