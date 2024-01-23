# https://leetcode.com/problems/find-if-array-can-be-sorted/ 

class Solution(object):
	def canSortArray(self, nums):
		def nBits(n):
			res = 0
			while n > 0:
				res += (n & 1)
				n >>= 1
			return res

		l = len(nums)
		while l > 0:
			lnew = 0
			for i in range(1, len(nums)):
				if nums[i - 1] > nums[i]:
					if nBits(nums[i]) != nBits(nums[i - 1]):
						return False
					else:
						nums[i], nums[i - 1] = nums[i - 1], nums[i]
						lnew = i
			l = lnew

		return True
