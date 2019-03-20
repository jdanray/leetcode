# https://leetcode.com/problem/relative-ranks/

class Solution:
	def findRelativeRanks(self, nums):
		N = len(nums)
		medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
		iranks = [i for i in sorted(range(N), key=lambda i: nums[i], reverse=True)]
		ranks = [""] * N

		for i, ir in enumerate(iranks):
			if i < len(medals):
				ranks[ir] = medals[i]
			else:
				ranks[ir] = str(i + 1)

		return ranks
