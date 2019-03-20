# leetcode.com/problems/contains-duplicate-iii/

class Solution:
	def containsNearbyAlmostDuplicate(self, nums, k, t):
		if not nums:
			return False

		indices = sorted(range(len(nums)), key=lambda i: nums[i])
		nbr = indices[0]
		for i in range(1, len(indices)):
			idx = indices[i]
			if abs(nums[idx] - nums[nbr]) > t:
				if abs(nums[idx] - nums[indices[i - 1]]) <= t:
					nbr = indices[i - 1]
				else:
					nbr = idx

			if 0 < abs(idx - nbr) <= k:
				return True

		return False
