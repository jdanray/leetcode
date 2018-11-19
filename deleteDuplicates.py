# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

"""
The solution to a problem instance is the given list without any duplicate numbers. So, for each number in the given list, include it in the solution iff it isn't a duplicate.

The given list is sorted. In a sorted list, a number is a duplicate iff it's equal to the previous number or the next number. So, for each number in the given list, test whether it's equal to the previous number or the next number. If it is, then skip it; exclude it from the solution. If it isn't, then include it.
"""

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
