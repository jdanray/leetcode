# https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/ 

class Solution(object):
	def largestInteger(self, num):
		odds = []
		evens = []
		heapq.heapify(odds)
		heapq.heapify(evens)

		n = num
		while n > 0:
			d = n % 10

			if d % 2 == 0:
				heapq.heappush(evens, d)
			else:
				heapq.heappush(odds, d)

			n //= 10

		p = 1
		res = 0
		while num > 0:
			d = num % 10

			if d % 2 == 0:
				r = heapq.heappop(evens)
			else:
				r = heapq.heappop(odds)

			res += p * r

			num //= 10
			p *= 10

		return res
