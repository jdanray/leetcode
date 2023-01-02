# https://leetcode.com/problems/closest-prime-numbers-in-range/

class Solution(object):
	def closestPrimes(self, left, right):
		isPrime = [True for _ in range(right + 1)]
		isPrime[0] = False
		isPrime[1] = False

		i = 2
		while i * i <= right:
			if isPrime[i]:
				for j in range(i * i, right + 1, i):
					isPrime[j] = False
			i += 1

		nums1 = -1
		res = [-1, -1]
		minDist = float('inf')
		for n in range(left, right + 1):
			if isPrime[n]:
				if nums1 != -1:
					d = n - nums1
					if d < minDist:
						minDist = d
						res = [nums1, n]
				nums1 = n

		return res
