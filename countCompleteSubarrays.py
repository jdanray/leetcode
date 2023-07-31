# https://leetcode.com/problems/count-complete-subarrays-in-an-array/ 

class Solution(object):
	def countCompleteSubarrays(self, nums):
		N = len(nums)
		ndistinct = len(set(nums))

		res = 0
		for i in range(N):
			seen = set()
			for j in range(i, N):
				seen.add(nums[j])

				if len(seen) > ndistinct:
					break

				if len(seen) == ndistinct:
					res += 1

		return res
