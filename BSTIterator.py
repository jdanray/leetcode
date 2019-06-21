# https://leetcode.com/problems/binary-search-tree-iterator/

class BSTIterator(object):
	def __init__(self, root):
		def inorder(root):
			if not root:
				return []
			return inorder(root.left) + [root.val] + inorder(root.right)
        
		self.elems = inorder(root)
		self.idx = 0

	def next(self):
		el = self.elems[self.idx]
		self.idx += 1
		return el

	def hasNext(self):
		return self.idx < len(self.elems)
