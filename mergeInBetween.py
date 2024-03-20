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

class Solution(object):
	def mergeInBetween(self, list1, a, b, list2):
		start = None	# the list1 node after which list2 starts
		tail = None	# the remaining "tail" of list1 that will be added to the end of list2
		i = 0
		node = list1
		while node:
			if i == a - 1:
				start = node

			if i == b + 1:
				tail = node

			node = node.next
			i += 1

		# if !start, then a == 0
		# we cannot return list1 as head
		if start:
			head = list1
			start.next = list2
		else:
			head = list2

		# find the end of list2
		# append the "tail" of list1 to the end of list2
		list2end = None
		node = list2
		while node:
			list2end = node
			node = node.next
		list2end.next = tail

		return head
