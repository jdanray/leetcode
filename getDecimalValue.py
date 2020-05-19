# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

class Solution(object):
	def getDecimalValue(self, head):
		res = 0
		while head:
			res *= 2
			res += head.val 
			head = head.next
		return res
