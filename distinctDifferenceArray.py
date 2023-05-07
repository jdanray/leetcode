# https://leetcode.com/problems/find-the-distinct-difference-array/ 

class Solution(object):
	def distinctDifferenceArray(self, nums):
		pre = collections.Counter()
		suf = collections.Counter(nums)
		pd = 0
		sd = len(suf)

		res = []
		for n in nums:
			pre[n] += 1
			if pre[n] == 1:
				pd += 1

			suf[n] -= 1
			if suf[n] == 0:
				sd -= 1

			res.append(pd - sd)

		return res
