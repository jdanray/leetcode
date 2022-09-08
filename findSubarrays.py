# https://leetcode.com/problems/find-subarrays-with-equal-sum/ 

class Solution(object):
	def findSubarrays(self, nums):
		s = 0
		seen = set()
		for i, n in enumerate(nums):
			s += n
            
			if i >= 2:
				s -= nums[i - 2]

			if i > 0:
				if s in seen:
					return True
				else:
					seen.add(s)

		return False

class Solution(object):
	def findSubarrays(self, nums):
		seen = set()
		for i in range(len(nums) - 1):
			s = nums[i] + nums[i + 1]
			if s in seen:
				return True
			else:
				seen.add(s)
                
		return False
