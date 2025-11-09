# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/

class Solution(object):
	def minimumDistance(self, nums):
		seen = collections.defaultdict(list)
		res = float('inf')
		for i, n in enumerate(nums):
			if len(seen[n]) == 2:
				res = min(res, (i - seen[n][0]) + (i - seen[n][1]) + (seen[n][1] - seen[n][0]))
				seen[n] = [seen[n][1], i]
			elif len(seen[n]) == 1:
				seen[n] = [seen[n][0], i]
			else:
				seen[n] = [i]

		return res if res != float('inf') else -1