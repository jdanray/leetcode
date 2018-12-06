# https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
	def lengthOfLIS(self, nums):
		if not nums:
			return 0

		memo = []
		for i, n in enumerate(nums):
			longest = 0
			for j in range(i):
				if nums[j] < n and memo[j] > longest:
					longest = memo[j]
			memo.append(longest + 1)
		return max(memo)
