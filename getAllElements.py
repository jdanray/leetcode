# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/ 

class Solution(object):
	def getAllElements(self, root1, root2):
		def qsort(root):
			if not root:
				return []

			return qsort(root.left) + [root.val] + qsort(root.right)

		def msort(lst1, lst2):
			i = 0
			j = 0
			res = []
			while i < len(lst1) and j < len(lst2):
				if lst1[i] < lst2[j]:
					res.append(lst1[i])
					i += 1
				else:
					res.append(lst2[j])
					j += 1

			if i < len(lst1):
				res += lst1[i:]

			if j < len(lst2):
				res += lst2[j:]

			return res

		sort1 = qsort(root1)
		sort2 = qsort(root2)

		return msort(sort1, sort2)
