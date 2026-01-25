# https://leetcode.com/problems/rotate-non-negative-elements/

class Solution(object):
	def rotateElements(self, nums, k):
		nonnegs = [n for n in nums if n >= 0]
		n = len(nonnegs)
		rot = [0 for _ in range(n)]
		for i in range(n):
			rot[(i - k) % n] = nonnegs[i]

		j = 0
		for i in range(len(nums)):
			if nums[i] >= 0:
				nums[i] = rot[j]
				j += 1

		return nums