# https://leetcode.com/problems/smallest-number-in-infinite-set/ 

class SmallestInfiniteSet(object):
	def __init__(self):
		self.m = 1
		self.included = [True for _ in range(10001)]
		self.pq = []
		heapq.heapify(self.pq)

	def popSmallest(self):
		if not self.pq:
			self.included[self.m] = False
			self.m += 1
			return self.m - 1
		else:
			res = heapq.heappop(self.pq)
			self.included[res] = False
			return res

	def addBack(self, num):
		if num < self.m and not self.included[num]:
			self.included[num] = True
			heapq.heappush(self.pq, num)
