# https://leetcode.com/problems/copy-list-with-random-pointer/ 

class Solution(object):
	def copyRandomList(self, head):
		newNode = {None: None}

		node = head
		while node:
			newNode[node] = Node(node.val)
			node = node.next

		node = head
		while node:
			newNode[node].next = newNode[node.next]
			newNode[node].random = newNode[node.random]
			node = node.next

		return newNode[head]
