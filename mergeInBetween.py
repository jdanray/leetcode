# https://leetcode.com/problems/merge-in-between-linked-lists/

class Solution(object):
	def mergeInBetween(self, list1, a, b, list2):
		head2 = list2
		tail2 = list2
		while head2:
			tail2 = head2
			head2 = head2.next

		head1 = list1
		for i in range(b + 2):
			if i == a - 1:
				stop1 = head1
			if i == b + 1:
				start1 = head1
			head1 = head1.next

		stop1.next = list2
		tail2.next = start1
		return list1
