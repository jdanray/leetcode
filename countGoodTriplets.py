# https://leetcode.com/problems/count-good-triplets/ 

class Solution(object):
	def countGoodTriplets(self, arr, a, b, c):
		N = len(arr)
		res = 0
		for i in range(N):
			for j in range(i + 1, N):
				for k in range(j + 1, N):
					if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
						res += 1
		return res
