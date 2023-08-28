# https://leetcode.com/problems/find-the-minimum-possible-sum-of-a-beautiful-array/

"""
Note: This problem is exactly the same as the problem found here: https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/

I copy-pasted the code from minimumSum.py:
"""

class Solution(object):
	def minimumPossibleSum(self, n, k):
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
