# https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/

class Solution(object):
	def getLargestOutlier(self, nums):
		idx = collections.defaultdict(list)
		for i, n in enumerate(nums):
			idx[n].append(i)

		t = sum(nums)
		res = float('-inf')
		for i, n in enumerate(nums):
			s = t - n
			if s % 2 == 0 and s // 2 in idx and (len(idx[s // 2]) > 1 or idx[s // 2][0] != i):
				res = max(res, n)

		return res