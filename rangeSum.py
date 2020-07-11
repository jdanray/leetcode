# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/

class Solution(object):
	def rangeSum(self, nums, n, left, right):
		MOD = 10**9 + 7
		N = len(nums)
		sums = []
		for i in range(N):
			s = 0
			for j in range(i, N):
				s += nums[j]
				sums.append(s)

		sums = sorted(sums)
		res = 0
		for i in range(left - 1, right):
			res += sums[i]
			res %= MOD

		return res

"""
After I solve a problem, I like to examine other people's solutions. This leetcode decided to use a priority queue: https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/discuss/730511/C%2B%2B-priority_queue-solution

I liked their idea so much that I decided to implement it in Python. Here is my Python implementation of their solution: 
"""

class Solution(object):
	def rangeSum(self, nums, n, left, right):
		MOD = 10**9 + 7
		N = len(nums)

		pq = []
		for i, n in enumerate(nums):
			heapq.heappush(pq, [n, i + 1])

		res = 0
		for j in range(1, right + 1):
			n, i = heapq.heappop(pq)

			if j >= left:
				res += n
				res %= MOD

			if i < N:
				heapq.heappush(pq, [n + nums[i], i + 1])

		return res
