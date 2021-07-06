# https://leetcode.com/problems/merge-two-sorted-lists

class Solution(object):
	def mergeTwoLists(self, l1, l2):
		if l1 and l2:
			if l1.val <= l2.val:
				l1.next = self.mergeTwoLists(l1.next, l2)
				return l1
			else:
				l2.next = self.mergeTwoLists(l1, l2.next)
				return l2

		return l1 if l1 else l2

class Solution(object):
	def mergeTwoLists(self, l1, l2):
		head = ListNode(-1)
		node = head
		while l1 and l2:
			if l1.val <= l2.val:
				node.next = l1
				l1 = l1.next
			else:
				node.next = l2
				l2 = l2.next
                
			node = node.next

		node.next = l1 if l1 else l2
		return head.next

# I revisited this old problem and came up with a much more elegant solution:

class Solution(object):
	def mergeTwoLists(self, l1, l2):
		if not l1:
			return l2        
		elif not l2:
			return l1        
		elif l1.val < l2.val:
			l1.next = self.mergeTwoLists(l1.next, l2)
			return l1
		else:
			l2.next = self.mergeTwoLists(l1, l2.next)
			return l2
