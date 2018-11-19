# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

class Solution(object):
	def removeDuplicates(self, nums):
		i = 0
		N = len(nums)
		while i < N:
			if i + 2 < N and nums[i] == nums[i + 2]:
				j = i + 2
				while j < N and nums[i] == nums[j]:
					j += 1
				k = i + 2
				l = j
				while l < N:
					nums[k] = nums[l]
					k += 1
					l += 1
				N -= (j - (i + 2))
				i += 2
			elif i + 1 < N and nums[i] == nums[i + 1]:
				i += 2
			else:
				i += 1
		return N
