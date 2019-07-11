# https://leetcode.com/problems/wiggle-sort-ii/ 

class Solution(object):
	def wiggleSort(self, nums):
		S = sorted(nums)
		j = len(S) - 1
		for i in range(1, len(nums), 2):
			nums[i] = S[j]
			j -= 1

		for i in range(0, len(nums), 2):
			nums[i] = S[j]
			j -= 1

# Pigeonhole sort
class Solution(object):
	def wiggleSort(self, nums):
		m = min(nums)
		N = max(nums) - m + 1
		holes = [0 for _ in range(N)]
		for n in nums: 
			holes[n - m] += 1

		c = len(holes) - 1
		for i in range(1, len(nums), 2):
			while holes[c] <= 0:
				c -= 1
			holes[c] -= 1
			nums[i] = c + m

		for i in range(0, len(nums), 2):
			while holes[c] <= 0:
				c -= 1
			holes[c] -= 1
			nums[i] = c + m
