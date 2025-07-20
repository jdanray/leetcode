# https://leetcode.com/problems/split-array-by-prime-indices/

class Solution(object):
	def splitArray(self, nums):
		N = len(nums)

		isPrime = dict((i, True) for i in range(N))
		isPrime[0] = isPrime[1] = False
		i = 2
		rt = N ** 0.5
		while i <= rt:
			for j in range(2, (N // i) + 1):
				isPrime[j * i] = False

			i += 1
			while not isPrime[i]:
				i += 1

		a = 0
		b = 0
		for i, n in enumerate(nums):
			if isPrime[i]:
				a += n
			else:
				b += n

		return abs(a - b)