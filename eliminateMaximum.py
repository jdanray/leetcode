# https://leetcode.com/problems/eliminate-maximum-number-of-monsters/ 

class Solution(object):
	def eliminateMaximum(self, dist, speed):
		t = sorted(float(d) / speed[i] for i, d in enumerate(dist))
		i = 1
		while i < len(t) and t[i] > i:
			i += 1
		return i

class Solution(object):
	def eliminateMaximum(self, dist, speed):
		N = len(dist)        
		minutes = sorted((dist[i] - 1) // speed[i] for i in range(N))
		for i, m in enumerate(minutes):
			if i > m:
				return i
		return N
