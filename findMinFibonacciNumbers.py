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

"""
After I solve a problem, I like to study other people's solutions to the problem. The program below is a Python program inspired by the following Java program: 

https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/discuss/585741/Java-Iterative-and-Intuitive-solution
"""

class Solution(object):
	def findMinFibonacciNumbers(self, k):
		a = 1
		b = 1
		while b < k:
			a, b = b, a + b

		res = 0
		while k > 0: 
			if b <= k:
				res += 1
				k -= b
			a, b = b - a, a

		return res 
