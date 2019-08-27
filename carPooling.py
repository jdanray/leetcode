# https://leetcode.com/problems/car-pooling/

class Solution(object):
	def carPooling(self, trips, capacity):
		pickup = collections.defaultdict(list)
		drop = collections.defaultdict(list)
		for (load, start, end) in trips:
			pickup[start].append(load)
			drop[end].append(load)

		LIM = 1000
		for loc in range(LIM + 1):
			for load in pickup[loc]:
				capacity -= load
			for load in drop[loc]:
				capacity += load
			if capacity < 0:
				return False  
            
		return True 
