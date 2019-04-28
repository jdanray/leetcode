# https://leetcode.com/problems/pancake-sorting/

class Solution:
	def reverse(self, A, k):
		i = 0
		k -= 1
		while i < k:
			A[i], A[k] = A[k], A[i]
			i += 1
			k -= 1

	def pancakeSort(self, A):
		flips = []
		for n in range(len(A), 0, -1):
			k = 1
			while A[k - 1] != n:
				k += 1

			self.reverse(A, k)
			self.reverse(A, n)
			flips.append(k)
			flips.append(n)

		return flips
