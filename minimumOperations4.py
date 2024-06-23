# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/ 

class Solution(object):
	def minimumOperations(self, nums):
		X = 3
		return sum(min(n % X, X - (n % X)) for n in nums)
