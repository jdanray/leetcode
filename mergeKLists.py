# https://leetcode.com/problems/merge-k-sorted-lists/

class Solution(object):
	def mergeKLists(self, lists):
		minheap = []
		for node in filter(None, lists):
			heapq.heappush(minheap, (node.val, node))

		if not minheap:
			return None
	
		fakeHead = ListNode(-1)
		cur = fakeHead
		while minheap:
			_, minode = heapq.heappop(minheap)
            
			cur.next = minode
            
			if minode.next: 
				heapq.heappush(minheap, (minode.next.val, minode.next))
                
			cur = cur.next
            
		return fakeHead.next 
