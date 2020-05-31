# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/

class Solution(object):
	def canBeEqual(self, target, arr):
		return len(target) == len(arr) and set(target) == set(arr)
