#  https://leetcode.com/problems/remove-element/

class Solution(object):
	def removeElement(self, nums, val):
		n = 0
		i = 0
		j = len(nums) - 1
		while i <= j:
			if nums[i] != val:
				n += 1
				i += 1
			elif nums[j] == val:
				j -= 1
			else:
				nums[i], nums[j] = nums[j], nums[i]
				i += 1
				j -= 1
				n += 1

		return n
