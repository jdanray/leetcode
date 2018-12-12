# https://leetcode.com/problems/palindrome-linked-list/

class Solution(object):
	def isPalindrome(self, head):
		digs = []
		while head:
			digs = [head.val] + digs
			head = head.next

		i = 0
		j = len(digs) - 1
		while i < j:
			if digs[i] != digs[j]:
				return False
			else:
				i += 1
				j -= 1

		return True
