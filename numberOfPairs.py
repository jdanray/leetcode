# https://leetcode.com/problems/maximum-number-of-pairs-in-array/ 

class Solution(object):
	def numberOfPairs(self, nums):
		count = collections.Counter(nums)

		p = sum(count[n] // 2 for n in count)
		u = sum(count[n] % 2 for n in count)
        
		return [p, u]
