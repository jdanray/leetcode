# https://leetcode.com/problems/continuous-subarrays/ 

from sortedcontainers import SortedList

class Solution(object):
	def continuousSubarrays(self, nums):
		CONT = 2
		sl = SortedList()
		i = 0
		res = 0
		for j, n in enumerate(nums):
			sl.add(n)

			while sl[-1] - n > CONT or n - sl[0] > CONT:
				sl.remove(nums[i])
				i += 1

			res += j - i + 1

		return res
