# https://leetcode.com/problems/closest-equal-element-queries/

class Solution(object):
	def solveQueries(self, nums, queries):
		indexes = collections.defaultdict(list)
		for i, n in enumerate(nums):
			indexes[n].append(i)

		res = []
		for q in queries:
			idx = indexes[nums[q]]

			if len(idx) == 1:
				res.append(-1)
				continue

			i = bisect.bisect_left(idx, q)
			l = (i - 1) % len(idx)
			r = (i + 1) % len(idx)

			dl = (idx[i] - idx[l]) % len(nums)
			dr = (idx[r] - idx[i]) % len(nums)

			res.append(min(dl, dr))

		return res