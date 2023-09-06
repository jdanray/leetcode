# https://leetcode.com/problems/linked-list-cycle/ 

class Solution(object):
	def hasCycle(self, head):
		seen = set()
		while head and head not in seen:
			seen.add(head)
			head = head.next
		return head in seen
