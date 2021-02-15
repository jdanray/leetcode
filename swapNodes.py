# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/ 

class Solution(object):
	def swapNodes(self, head, k):
		n = 0
		left = None
		dummy = head
		while dummy:
			n += 1
			if n == k:
				left = dummy
			dummy = dummy.next

		i = 0
		dummy = head
		while dummy:
			if i == n - k:
				dummy.val, left.val = left.val, dummy.val
			i += 1
			dummy = dummy.next

		return head

"""
After I solve a problem, I like to examine other people's solutions. I discovered the following one-pass solution:

https://leetcode.com/problems/swapping-nodes-in-a-linked-list/discuss/1009800/C%2B%2B-One-Pass

The above program is written in C++. I translated the program into Python:
"""

class Solution(object):
	def swapNodes(self, head, k):
		left = None
		right = None
		dummy = head
		while dummy:
			if right:
				right = right.next

			k -= 1
			if k == 0:
				left = dummy
				right = head

			dummy = dummy.next
	
		left.val, right.val = right.val, left.val
		return head
