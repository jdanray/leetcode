# https://leetcode.com/contest/weekly-contest-148/problems/decrease-elements-to-make-array-zigzag/

"""
The strategy is simple:
nums is a zigzag array if it satisfies one of two conditions. 
(Let's say that a zigzag array can be a zig array or a zag array.)
So: 
Try to transform nums into a zig array using only the necessary number of moves
Try to transform nums ibto a zag array using only the necessary number of moves  
Pick the transformation that requires the least number of moves
"""

class Solution(object):
	def movesToMakeZigzag(self, nums):
		zignums = list(nums)
		zagnums = list(nums)
		zig = 0
		zag = 0
		for i in range(len(nums) - 1):
			if i % 2 == 0:
				if zignums[i] <= zignums[i+1]:
					d = (zignums[i+1] - zignums[i]) + 1
					zignums[i+1] -= d
					zig += d
				if zagnums[i] >= zagnums[i+1]:
					d = (zagnums[i] - zagnums[i+1]) + 1
					zagnums[i] -= d
					zag += d
			elif i % 2 == 1:
				if zignums[i] >= zignums[i+1]:
					d = (zignums[i] - zignums[i+1]) + 1
					zignums[i] -= d
					zig += d
				if zagnums[i] <= zagnums[i+1]:
					d = (zagnums[i+1] - zagnums[i]) + 1
					zagnums[i+1] -= d
					zag += d 
                    
		return min(zig, zag)
