# https://leetcode.com/problems/count-special-quadruplets/

class Solution(object):
	def countQuadruplets(self, nums):
		N = len(nums)

		sums = collections.defaultdict(list)
		for a in range(N):
			for b in range(a + 1, N):
				for c in range(b + 1, N):
					sums[nums[a] + nums[b] + nums[c]].append(c)

		res = 0
		for d in range(3, N):
			for idx in sums[nums[d]]:
				if d > idx:
					res += 1

		return res
