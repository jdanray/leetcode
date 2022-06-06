# https://leetcode.com/problems/replace-elements-in-an-array/

class Solution(object):
	def arrayChange(self, nums, operations):
		val = collections.defaultdict(int)
		idx = collections.defaultdict(int)
		for i, n in enumerate(nums):
			idx[n] = i
			val[i] = n

		for (cur, new) in operations:
			i = idx[cur]
			val[i] = new
			idx[new] = i

		return [val[i] for i in range(len(nums))]
