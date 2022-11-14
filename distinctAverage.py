# https://leetcode.com/problems/number-of-distinct-averages/

class Solution(object):
	def distinctAverages(self, nums):
		nums = sorted(nums)
		avgs = set()
		i = 0
		j = len(nums) - 1
		while i < j:
			a = (1.0 * nums[i] + nums[j]) / 2

			avgs.add(a)

			i += 1
			j -= 1

		return len(avgs)
