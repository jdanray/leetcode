# https://leetcode.com/problems/numbers-with-same-consecutive-differences/

class Solution(object):
	def numsSameConsecDiff(self, N, K):
		if N == 1:
			return list(range(10))

		m = 10 ** (N - 1)
		stack = [[d * m, d, m // 10] for d in range(1, 10)]
		res = set()
		while stack:
			num, d, m = stack.pop()

			if m == 0:
				res.add(num)
				continue

			a = d + K
			if a < 10:
				stack.append([num + a * m, a, m // 10])

			b = d - K
			if b >= 0:
				stack.append([num + b * m, b, m // 10])

		return list(res)
