# https://leetcode.com/problems/palindrome-linked-list/

class Solution(object):
	def isPalindrome(self, head):
		nums = []
		while head:
			nums.append(head.val)
			head = head.next

		i = 0
		j = len(nums) - 1
		while i < j and nums[i] == nums[j]:
			i += 1
			j -= 1

		return i >= j
