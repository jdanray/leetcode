# https://leetcode.com/problems/grumpy-bookstore-owner/

class Solution(object):
	def maxSatisfied(self, customers, grumpy, X):
		cur = sum(c for i, c in enumerate(customers) if grumpy[i] == 0 or i < X)
		M = cur
		i = 0
		for j in range(X, len(customers)):
			if grumpy[j] == 1:
				cur += customers[j]

			if grumpy[i] == 1:
				cur -= customers[i]

			M = max(M, cur)
			i += 1

		return M

class Solution(object):
	def maxSatisfied(self, customers, grumpy, minutes):
		s = sum(c for i, c in enumerate(customers) if grumpy[i] == 0)
		res = s
		for i in range(len(customers)):
			if grumpy[i] == 1:
				s += customers[i]

			if i >= minutes and grumpy[i - minutes] == 1:
				s -= customers[i - minutes]

			res = max(res, s)

		return res
