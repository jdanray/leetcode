# https://leetcode.com/problems/brick-wall/description/

class Solution(object):
	def leastBricks(self, wall):
		m = 0
		count = dict()
		for row in wall:
			l = 0
			for i in range(len(row) - 1):
				l += row[i]
				if l not in count:
					count[l] = 0
				count[l] += 1
				if count[l] > m:
					m = count[l]
		return len(wall) - m
