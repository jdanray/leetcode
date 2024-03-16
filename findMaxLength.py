# https://leetcode.com/problems/contiguous-array/ 

class Solution(object):
	def findMaxLength(self, nums):
		m = {0: 0}
		l = 0
		res = 0
		for i, n in enumerate(nums):
			if n == 1:
				l += 1
			else:
				l -= 1

			if l in m:
				res = max(res, i - m[l] + 1)
			else:
				m[l] = i

		return res if res % 2 == 0 else res - 1
