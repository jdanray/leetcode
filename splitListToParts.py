# https://leetcode.com/problems/split-linked-list-in-parts/

class Solution:
	def splitListToParts(self, root, k):
		l = 0
		node = root
		while node:
			l += 1
			node = node.next

		q = l // k
		r = l % k
		parts = [None for _ in range(k)]
		node = root
		tail = None
		for i in range(k):
			n = q
			if r > 0:
				n += 1
				r -= 1

			parts[i] = node
			for _ in range(n):
				tail = node
				node = node.next
                
			if tail:
				tail.next = None

		return parts
