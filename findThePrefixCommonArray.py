# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/ 

class Solution(object):
	def findThePrefixCommonArray(self, A, B):
		N = len(A)

		seen = collections.Counter()
		res = [0 for _ in range(N)]
		for i in range(N):
			seen[A[i]] += 1 
			seen[B[i]] += 1

			if i > 0:
				res[i] = res[i - 1]

			if seen[A[i]] == 2:
				res[i] += 1

			if B[i] != A[i] and seen[B[i]] == 2:
				res[i] += 1

		return res

"""
After I solve a problem, I like to see other people's problems. I was impressed by this C++ solution:

https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/discuss/3466676/Frequency-array-solution-explained-or-O(n)-Time-and-Space-or-C%2B%2B

So, I rewrote the program in Python:
"""

class Solution(object):
	def findThePrefixCommonArray(self, A, B):
		seen = collections.Counter()
		c = 0
		res = []
		for i in range(len(A)):
			seen[A[i]] += 1 
			if seen[A[i]] == 2:
				c += 1

			seen[B[i]] += 1
			if seen[B[i]] == 2:
				c += 1

			res.append(c)

		return res
