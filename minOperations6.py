# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/ 

class Solution(object):
	def minOperations(self, nums, x):
		N = len(nums)

		ops = collections.defaultdict(int)
		s = 0
		for i, n in enumerate(nums):
			s += n
			ops[s] = i + 1

		if x in ops:
			res = ops[x]
		else:
			res = float('inf')

		s = 0
		for j in range(N - 1, -1, -1):
			s += nums[j]

			if x - s in ops and j + 1 > ops[x - s]:
				res = min(res, (N - j) + ops[x - s])

			if x == s:
				res = min(res, N - j)

		return -1 if res == float('inf') else res
