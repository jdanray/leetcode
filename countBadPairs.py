# https://leetcode.com/problems/count-number-of-bad-pairs/ 

"""
A bad pair is a pair of indices (i, j), where i < j and j - i != nums[j] - nums[i]. For any bad pair, there is an index j that is the second member of the pair, and an index i that is the first member. To count all bad pairs, iterate over each num and count the bad pairs that it is the second member of. 

Define a good pair. A good pair is a pair of indices (i, j), where i < j and j - i == nums[j] - nums[i]. For the j-th num, the number of bad pairs is the total number of pairs, minus the number of good pairs. To keep account of the number of good pairs, rearrange the equation to j - nums[j] == i - nums[i], and count all i - nums[i].
"""

class Solution(object):
	def countBadPairs(self, nums):
		count = collections.Counter()
		res = 0
		for i, n in enumerate(nums):
			res += i - count[i - n]
			count[i - n] += 1
            
		return res
