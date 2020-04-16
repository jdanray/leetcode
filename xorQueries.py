# https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution(object):
	def xorQueries(self, arr, queries):
		N = len(arr)
		xor = [-1 for _ in range(N)]
		xor[0] = arr[0]
		for i in range(1, N):
			xor[i] = xor[i - 1] ^ arr[i]

		res = []
		for (j, k) in queries:
			if j == 0:
				res.append(xor[k])
			else:
				res.append(xor[j - 1] ^ xor[k])

		return res
