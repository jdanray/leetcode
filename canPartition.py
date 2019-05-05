# https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
	def canPartition(self, nums):
		total = sum(nums)

		if total % 2 == 1:
			return False

		total //= 2

		can = collections.defaultdict(bool)
		can[0] = True
		for n in nums:
			for s in range(total, 0, -1):
				can[s] |= can[s - n]

		return can[total]
