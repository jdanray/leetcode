# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/ 

# Note: This program also solves the problem found here: https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/

class Solution(object):
	def resultsArray(self, nums, k):
		asc = 0
		res = []
		for i, n in enumerate(nums):
			if i > 0 and n == nums[i - 1] + 1:
				asc += 1
			else:
				asc = 1

			if i < k - 1:
				continue

			if asc >= k:
				res.append(n)
			else:
				res.append(-1)

		return res
