# https://leetcode.com/problems/rotate-list/

class Solution(object):
	def rotateRight(self, head, k):
		nums = []
		node = head
		while node:
			nums.append(node.val)
			node = node.next

		rot = [None] * len(nums)
		for i, n in enumerate(nums):
			j = (i + k) % len(nums)
			rot[j] = n

		node = head
		i = 0
		while node:
			node.val = rot[i]
			node = node.next
			i += 1

		return head
