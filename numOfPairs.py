# https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/

class Solution(object):
	def numOfPairs(self, nums, target):
		N = len(nums)
		count = collections.Counter(nums[i] + nums[j] for i in range(N) for j in range(N) if i != j)
		return count[target]
