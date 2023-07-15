# https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/ 

from sortedcontainers import SortedList

class Solution(object):
	def busiestServers(self, k, arrival, load):
		count = collections.Counter()
		avail = SortedList(list(range(k)))
		busy = []
		for (i, a) in enumerate(arrival):
			while busy and busy[0][0] <= a:
				_, s = heapq.heappop(busy)
				avail.add(s)

			if avail:
				j = avail.bisect_left(i % k)
				if j >= len(avail):
					s = avail[0]
				else:
					s = avail[j]

				avail.remove(s)
				heapq.heappush(busy, (a + load[i], s))		
				count[s] += 1

		maxc = max(count.values())
		return [s for s in range(k) if count[s] == maxc]
