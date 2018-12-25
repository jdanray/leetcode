# https://leetcode.com/problems/intersection-of-two-linked-lists/description/

class Solution(object):
	def getIntersectionNode(self, headA, headB):
		seen = set()
		while headA:
			seen.add(headA)
			headA = headA.next
		while headB:
			if headB in seen:
				return headB
			headB = headB.next
