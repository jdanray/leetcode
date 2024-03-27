# https://leetcode.com/problems/most-frequent-ids/ 

class Solution(object):
	def mostFrequentIDs(self, nums, freq):
		count = collections.Counter()
		pq = []
		res = []
		for i, n in enumerate(nums):
			count[n] += freq[i]
			heapq.heappush(pq, (-count[n], n))

			while pq and -pq[0][0] != count[pq[0][1]]:
				heapq.heappop(pq)

			if pq:
				res.append(-pq[0][0])
			else:
				res.append(0)

		return res
