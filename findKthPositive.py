# https://leetcode.com/problems/kth-missing-positive-number/

class Solution(object):
	def findKthPositive(self, arr, k):
		m = 1
		for n in arr:
			while m < n and k > 0:
				m += 1
				k -= 1

			if k == 0:
				return m - 1

			m += 1

		return arr[-1] + k
