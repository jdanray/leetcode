# https://leetcode.com/problems/reorder-list/ 

class Solution(object):
	def reorderList(self, head):
		lst = []
		while head:
			lst.append(head)
			head = head.next
	
		i = 0
		j = len(lst) - 1
		while j > 0 and i <= j:
			if i + 1 == j: 
				lst[j].next = None
			else:
				lst[j].next = lst[i + 1]

			if i == j:
				lst[i].next = None
			else:
				lst[i].next = lst[j]

			i += 1
			j -= 1

# I revisited this old problem and came up with a more elegant solution: 

class Solution(object):
	def reorderList(self, head):
		lst = []
		while head:
			lst.append(head)
			head = head.next

		N = len(lst)
		for i in range(N // 2):
			lst[i].next = lst[N - i - 1]
			lst[N - i - 1].next = lst[i + 1]

		lst[N // 2].next = None
