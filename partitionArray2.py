# https://leetcode.com/problems/partition-array-into-k-distinct-groups/

class Solution(object):
	def partitionArray(self, nums, k):
		if len(nums) % k != 0:
			return False

		count = collections.Counter(nums)
		return all(count[n] <= len(nums) // k for n in count)