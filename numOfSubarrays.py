# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

class Solution(object):
	def numOfSubarrays(self, arr, k, threshold):
		res = 0
		targ = threshold * k
		s = 0
		for i, n in enumerate(arr):
			s += n
			if i >= k:
				s -= arr[i - k]

			if i >= k - 1 and s >= targ:
				res += 1

		return res
