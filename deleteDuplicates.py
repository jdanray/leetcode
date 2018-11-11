# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

class Solution:
	def deleteDuplicates(self, head, prev=None):
		"""
		Include head in the solution or not?
		Include head iff head isn't a duplicate
		head is a duplicate iff its previous node or its next node has the same value
		"""
		if not head:
			return None
		elif (prev and prev.val == head.val) or (head.next and head.next.val == head.val):
			return self.deleteDuplicates(head.next, head)
		else:
			head.next = self.deleteDuplicates(head.next, head)
			return head
