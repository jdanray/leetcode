# https://leetcode.com/problems/smallest-absent-positive-greater-than-average/

class Solution(object):
	def smallestAbsent(self, nums):
		avg = float(sum(nums)) / len(nums)
		nums = set(nums)
		res = max(int(avg + 1), 1)
		while res in nums:
			res += 1
		return res