# https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/ 

# O(N) 
class Solution(object):
	def longestAlternatingSubarray(self, nums, threshold):
		N = len(nums)

		sub = 0
		res = 0
		for r in range(N):
			if nums[r] > threshold:
				sub = 0
			elif sub > 0 and r > 0 and nums[r - 1] % 2 != nums[r] % 2: 
				sub += 1
			elif nums[r] % 2 == 0:
				sub = 1
			else:
				sub = 0

			res = max(res, sub)

		return res

# O(N**2)
class Solution(object):
	def longestAlternatingSubarray(self, nums, threshold):
		N = len(nums)

		res = 0
		for l in range(N):
			if nums[l] > threshold or nums[l] % 2 != 0:
				continue

			r = l + 1
			while r < N and nums[r] <= threshold and nums[r] % 2 != nums[r - 1] % 2:
				r += 1

			res = max(res, r - l)

		return res
