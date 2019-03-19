# https://leetcode.com/problems/maximize-distance-to-closest-person/

class Solution(object):
	def maxDistToClosest(self, seats):
		ones = [i for i in range(len(seats)) if seats[i] == 1]

		maxd = max(ones[0], len(seats) - 1 - ones[-1])

		for i in range(1, len(ones)):
			maxd = max(maxd, (ones[i] - ones[i - 1]) // 2)

		return maxd
