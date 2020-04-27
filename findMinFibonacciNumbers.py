# https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

class Solution(object):
	def findMinFibonacciNumbers(self, k):
		fib = [1, 1]
		while fib[-1] < k:
			fib.append(fib[-1] + fib[-2])

		def helper(k, i):
			while fib[i] > k:
				i -= 1

			if fib[i] == k:
				return 1
			else:
				return 1 + helper(k - fib[i], i)

		return helper(k, len(fib) - 1)
