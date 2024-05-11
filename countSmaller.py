# https://leetcode.com/problems/count-of-smaller-numbers-after-self/ 

from sortedcontainers import SortedList

class Solution(object):
	def countSmaller(self, nums):
		N = len(nums)
        
		sl = SortedList()
		counts = [0 for _ in range(N)]
		for i in range(N - 1, -1, -1):
			counts[i] = sl.bisect_left(nums[i])
			sl.add(nums[i])
            
		return counts
