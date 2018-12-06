# https://leetcode.com/problems/linked-list-components/

class Solution(object):
	def numComponents(self, head, G):
		G = set(G)
		prev = -1
		n = 0
		while head:
			if head.val in G and prev not in G:
				n += 1
			prev = head.val
			head = head.next
		return n
