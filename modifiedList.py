# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/ 

class Solution(object):
	def modifiedList(self, nums, head):
		nums = set(nums)

		fakeHead = ListNode(-1)
		fakeHead.next = head

		prev = fakeHead
		node = head
		while node:
			if node.val in nums:
				prev.next = node.next
			else:
				prev = node
			node = node.next

		return fakeHead.next
