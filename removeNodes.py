# https://leetcode.com/problems/remove-nodes-from-linked-list/ 

class Solution(object):
	def removeNodes(self, head):
		stack = []
		while head:
			while stack and stack[-1].val < head.val:
				stack.pop()
                
			stack.append(head)
			head = head.next

		for i in range(len(stack) - 1):
			stack[i].next = stack[i + 1]

		return stack[0]
