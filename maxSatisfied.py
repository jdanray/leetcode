# https://leetcode.com/problems/grumpy-bookstore-owner/

class Solution(object):
	def maxSatisfied(self, customers, grumpy, X):
		cur = M = sum(c for i, c in enumerate(customers) if grumpy[i] == 0 or i < X)
		i = 0
		for j in range(X, len(customers)):
			if grumpy[j] == 1:
				cur += customers[j]

			if grumpy[i] == 1:
				cur -= customers[i]

			M = max(M, cur)
			i += 1

		return M
