# https://leetcode.com/problems/trionic-array-i/

class Solution(object):
	def isTrionic(self, nums):
		N = len(nums)

		p = 1
		while p < N and nums[p - 1] < nums[p]:
			p += 1

		if p >= N or nums[p - 1] == nums[p] or p == 1:
			return False

		q = p
		while q < N and nums[q - 1] > nums[q]:
			q += 1

		if q >= N or nums[q - 1] == nums[q] or q == p:
			return False

		r = q
		while r < N and nums[r - 1] < nums[r]:
			r += 1

		return r == N