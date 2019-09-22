# https://leetcode.com/problems/minimum-absolute-difference/

class Solution(object):
	def minimumAbsDifference(self, arr):
		arr = sorted(arr)
		maxd = float('inf')
		res = []
		for i in range(len(arr) - 1):
			d = abs(arr[i + 1] - arr[i])
			if d < maxd:
				res = [[arr[i], arr[i + 1]]]
				maxd = d
			elif d == maxd:
				res.append([arr[i], arr[i + 1]])
		return res
