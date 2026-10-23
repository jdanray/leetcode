# https://leetcode.com/problems/find-subtree-sizes-after-changes/

class Solution(object):
	def findSubtreeSizes(self, parent, s):
		root = 0

		children = collections.defaultdict(set)
		for u in range(len(parent)):
			children[parent[u]].add(u)
 
		newChildren = collections.defaultdict(set)
		stack = [[root, dict()]]
		while stack:
			u, seen = stack.pop()

			if s[u] in seen:
				newChildren[seen[s[u]]].add(u)
			else:
				newChildren[parent[u]].add(u)

			newSeen = dict(seen)
			newSeen[s[u]] = u

			for v in children[u]:
				stack.append([v, newSeen])

		res = [1 for _ in range(len(parent))]
		def size(u):
			for v in newChildren[u]:
				res[u] += size(v)
			return res[u]

		size(root)
		return res