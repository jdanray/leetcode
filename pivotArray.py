# https://leetcode.com/problems/partition-array-according-to-given-pivot/ 

class Solution(object):
	def pivotArray(self, nums, pivot):
		lt = []
		eq = []
		gt = []
		for n in nums:
			if n < pivot:
				lt.append(n)
			elif n == pivot:
				eq.append(n)
			else:
				gt.append(n)

		return lt + eq + gt
