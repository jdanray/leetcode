# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/ 

class Solution(object):
	def minOperations(self, nums):
		count = collections.Counter(nums)
		res = 0
		for n in count:
			if count[n] == 1:
				return -1

			res += (count[n] // 3) + (count[n] % 3 != 0)

		return res
