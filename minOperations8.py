# https://leetcode.com/problems/minimum-operations-to-collect-elements/ 

class Solution(object):
	def minOperations(self, nums, k):
		N = len(nums)
        
		seen = set()
		for i in range(N - 1, -1, -1):
			seen.add(nums[i])
            
			if all(n in seen for n in range(1, k + 1)):
				return N - i

"""
After I solve a problem, I like to study other people's solutions. I found a more time-efficient solution here: 

https://leetcode.com/problems/minimum-operations-to-collect-elements/discuss/4109943/Count-Unique-Numbers

I rewrote it from C++ to Python:
"""

class Solution(object):
	def minOperations(self, nums, k):
		N = len(nums)
        
		seen = set()
		found = 0
		for i in range(N - 1, -1, -1):
			if nums[i] <= k and nums[i] not in seen:
				seen.add(nums[i])
				found += 1

			if found == k:
				return N - i
