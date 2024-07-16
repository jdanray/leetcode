# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/ 

class Solution(object):
	def getDirections(self, root, startValue, destValue):
		def bfs(val):
			queue = collections.deque([[root, '']])
			while queue:
				u, p = queue.popleft()

				if not u:
					continue

				if u.val == val:
					return p

				queue.append([u.left, p + 'L'])
				queue.append([u.right, p + 'R'])

		s = bfs(startValue)
		d = bfs(destValue)

		i = 0
		while i < len(s) and i < len(d) and s[i] == d[i]:
			i += 1

		return 'U' * (len(s) - i) + d[i:]
