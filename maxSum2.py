# https://leetcode.com/problems/max-pair-sum-in-an-array/ 

class Solution(object):
	def maxSum(self, nums):
		maxDigit = collections.defaultdict(list)
		for num in nums:
			n = num
			m = 0
			while n > 0:
				m = max(m, n % 10)
				n //= 10
 
			maxDigit[m].append(num)

		res = -1
		for d in maxDigit:
			first = -1
			second = -1
			for n in maxDigit[d]:
				if n > first:
					first, second = n, first
				elif n > second:
					second = n

			if first != -1 and second != -1:
				res = max(res, first + second)

		return res

"""
After I solve a problem, I like to study other people's solutions. One leetcoder arrived at a solution that is similar to mine, but is cleaner and more efficient:

https://leetcode.com/problems/max-pair-sum-in-an-array/discuss/3901608/O(n-log-n)

You don't need to keep track of all numbers with the same maximum digit. You only need to record the largest number with that digit. I rewrote the leetcoder's C++ program into Python:
"""

class Solution(object):
	def maxSum(self, nums):
		maxDigit = collections.defaultdict(int)
		res = -1
		for num in nums:
			n = num
			m = 0
			while n > 0:
				m = max(m, n % 10)
				n //= 10

			if maxDigit[m]:
				res = max(res, maxDigit[m] + num) 
 
			maxDigit[m] = max(maxDigit[m], num)

		return res
