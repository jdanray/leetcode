# https://leetcode.com/problems/query-kth-smallest-trimmed-number/ 

class Solution(object):
	def smallestTrimmedNumbers(self, nums, queries):
		M = len(nums)
		N = len(nums[0])

		trim = [[] for _ in range(N)]
		for s in nums:
			n = 0
			for i, c in enumerate(s[::-1]):
				n += (10 ** i) * int(c)
				trim[i].append(n)

		for i in range(N):
			trim[i] = sorted(list(range(M)), key=lambda j: trim[i][j])

		return [trim[t - 1][k - 1] for (k, t) in queries]
