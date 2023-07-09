# https://leetcode.com/problems/relocate-marbles/ 

class Solution(object):
	def relocateMarbles(self, nums, moveFrom, moveTo):
		occupied = {n: True for n in nums}
		for (i, f) in enumerate(moveFrom):
			t = moveTo[i]
			occupied[f] = False
			occupied[t] = True

		return sorted([n for n in occupied if occupied[n]]) 
