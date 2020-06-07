# https://leetcode.com/problems/the-k-strongest-values-in-an-array/ 

class Solution(object):
	def getStrongest(self, arr, k):
		N = len(arr)
		arr = sorted(arr)
		m = (N - 1) // 2
		median = arr[m]

		strong = sorted(arr, key=lambda a: abs(a - median))

		return strong[::-1][:k]
