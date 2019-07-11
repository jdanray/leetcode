# https://leetcode.com/problems/sort-list/ 

class Solution(object):
	def merge(self, left, right):
		fakeHead = ListNode(0)
		p = fakeHead
		while left and right:
			if left.val < right.val:
				p.next = left
				left = left.next
			else:
				p.next = right
				right = right.next
			p = p.next

		if left:
			p.next = left
		if right:
			p.next = right
	
		return fakeHead.next	

	def sortList(self, head):
		if not head or not head.next:
			return head

		fast = head
		mid = head
		prev = None
		while fast and fast.next:
			fast = fast.next.next
			prev = mid
			mid = mid.next

		prev.next = None
		left = self.sortList(head)
		right = self.sortList(mid)
		lst = self.merge(left, right)

		return lst
