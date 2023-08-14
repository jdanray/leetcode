# https://leetcode.com/problems/kth-largest-element-in-an-array/

"""
Complexity:

Time: If pushing a number onto PQ causes PQ's size to become greater than K, then we pop the smallest element off PQ. So, because the size of PQ will not stay greater than K, pushing and popping is O(lg(K)). And, because we push each of the N numbers, the time-complexity is O(N * log(K)). However, K == N in the worst case.

Space: We create one data structure (ie, PQ), and PQ may not contain more than K elements. So, the space-complexity is O(K). However, K == N in the worst case. 
"""

class Solution(object):
	def findKthLargest(self, nums, k):
		pq = []
		for n in nums:
			heapq.heappush(pq, n)

			if len(pq) > k:
				heapq.heappop(pq)

		return pq[0]

"""
Complexity:
Time: O(N)
Space: O(N)
"""

class Solution(object):
	def findKthLargest(self, nums, k):
		count = collections.Counter(nums)
		for n in range(max(nums), min(nums) - 1, -1):
			if count[n] < k:
				k -= count[n]
			else:
				return n
