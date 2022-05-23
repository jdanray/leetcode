# https://leetcode.com/problems/largest-3-same-digit-number-in-string/ 

class Solution(object):
	def largestGoodInteger(self, num):
		N = len(num)

		res = ''
		for i in range(N - 2):
			if num[i] == num[i + 1] == num[i + 2]:
				res = max(res, num[i])

		return 3*res if res else res
