# https://leetcode.com/problems/minimum-genetic-mutation/

class Solution(object):
	def minMutation(self, start, end, bank):
		chars = ["A", "C", "G", "T"]
		bank = set(bank)
		seen = set()
		queue = [[start, 0]]
		while queue:
			node, dist = queue.pop(0)

			if node == end:
				return dist

			for i, x in enumerate(node): 
				for y in chars:
					if x != y:
						newnode = node[:i] + y + node[i + 1:]
						if newnode in bank and newnode not in seen:
							seen.add(newnode)
							queue.append([newnode, dist + 1])

		return -1
