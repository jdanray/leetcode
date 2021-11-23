# https://leetcode.com/problems/k-th-smallest-prime-fraction/ 

class Solution(object):
	def kthSmallestPrimeFraction(self, arr, k):
		N = len(arr)

		s = []
		for i in range(N):
			for j in range(i + 1, N):
				s.append((1.0 * arr[i] / arr[j], [arr[i], arr[j]]))

		s = sorted(s)
		return s[k - 1][1]
