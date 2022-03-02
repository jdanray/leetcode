# https://leetcode.com/problems/reverse-linked-list-ii/ 

class Solution(object):
	def reverseBetween(self, head, left, right):
		def reverse(f, t):
			if f == t:
				return f
			else:
				t.next = reverse(f, prev[t])
				return t

		prev = {}
		pre = None
		cur = head
		idx = 1
		while cur:
			prev[cur] = pre
			pre = cur

			if idx == left:
				front = cur
			if idx == right:
				tail = cur
			idx += 1

			cur = cur.next

		preFront = prev[front]
		nextTail = tail.next

		reverse(front, tail)

		if preFront: 
			preFront.next = tail
		front.next = nextTail

		return tail if head == front else head
