# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/

class Solution(object):
	def findXSum(self, nums, k, x):
		count = collections.Counter()
		res = []
		for i, n in enumerate(nums):
			count[n] += 1

			if i >= k:
				count[nums[i - k]] -= 1

			if i >= k - 1:
				pq = []
				for el in count:
					heapq.heappush(pq, (-count[el], -el))

				j = 0
				res.append(0)
				while pq and j < x:
					c, el = heapq.heappop(pq)
					res[-1] += (c * el)
					j += 1

		return res