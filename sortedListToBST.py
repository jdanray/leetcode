# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

class Solution(object):
	def sortedListToBST(self, head):
		if not head:
			return None
		elif not head.next:
			return TreeNode(head.val)

		N = 0
		cur = head
		while cur:
			N += 1
			cur = cur.next

		m = N // 2
		prev = None
		mid = head
		while m > 0:
			prev = mid
			mid = mid.next
			m -= 1

		prev.next = None

		root = TreeNode(mid.val)
		root.left = self.sortedListToBST(head)
		root.right = self.sortedListToBST(mid.next)

		return root
