# https://leetcode.com/problems/arithmetic-subarrays/ 

class Solution(object):
	def checkArithmeticSubarrays(self, nums, l, r):
		res = []
		for i in range(len(l)):
			s = sorted(nums[l[i]:r[i] + 1])
			d = s[1] - s[0]
			res.append(all(s[j] - s[j - 1] == d for j in range(2, len(s))))
		return res
