# https://leetcode.com/problems/linked-list-random-node/ 

class Solution(object):
	def __init__(self, head):
		self.lst = []
		while head:
			self.lst.append(head)
			head = head.next

	def getRandom(self):
		return self.lst[random.randrange(0, len(self.lst))].val
