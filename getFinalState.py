# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/ 

class Solution(object):
	def getFinalState(self, nums, k, multiplier):
		pq = [(n, i) for i, n in enumerate(nums)]
		heapq.heapify(pq)
		for _ in range(k):
			n, i = heapq.heappop(pq)
			m = n * multiplier
			heapq.heappush(pq, (m, i))
			nums[i] = m
            
		return nums
