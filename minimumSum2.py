# https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/ 

class Solution(object):
	def minimumSum(self, n, k):
		unavail = set()
		l = 1
		res = 0
		for _ in range(n):
			while l in unavail:
				l += 1

			unavail.add(k - l)
			res += l
			l += 1

		return res
