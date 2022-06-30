# https://leetcode.com/problems/removing-minimum-number-of-magic-beans/ 

class Solution(object):
	def minimumRemoval(self, beans):
		N = len(beans)
		beans = sorted(beans)

		s = [0 for _ in range(N)]
		s[0] = beans[0]
		c = [1 for _ in range(N)]
		for i in range(1, N):
			s[i] = s[i - 1] + beans[i]
			if beans[i] == beans[i - 1]:
				c[i] += c[i - 1]

		res = float('inf')
		for i, b in enumerate(beans):
			left = s[i] - (c[i] * b)
			right = (s[-1] - s[i]) - (b * (N - i - 1))
			res = min(res, left + right)

		return res
