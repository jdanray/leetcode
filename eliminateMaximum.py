# https://leetcode.com/problems/eliminate-maximum-number-of-monsters/ 

class Solution(object):
	def eliminateMaximum(self, dist, speed):
		N = len(dist)        
		minutes = sorted((dist[i] - 1) // speed[i] for i in range(N))
		for i, m in enumerate(minutes):
			if i > m:
				return i
		return N
