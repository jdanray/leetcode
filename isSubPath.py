# https://leetcode.com/problems/linked-list-in-binary-tree/

class Solution(object):
	def isSubPath(self, head, root):
		stack = [[root, [head]]]
		while stack:
			node, links = stack.pop()

			if not node:
				continue

			newlinks = [head]
			for l in links:
				if node.val == l.val:
					if not l.next:
						return True
					else:
						newlinks += [l.next]

			stack.append([node.left, newlinks])
			stack.append([node.right, newlinks])

		return False

"""
After I solve a problem, I like to study other people's solutions. Here are some solutions that I thought deserved preservation:

Java:

    public boolean isSubPath(ListNode head, TreeNode root) {
        if (head == null) return true;
        if (root == null) return false;
        return dfs(head, root) || isSubPath(head, root.left) || isSubPath(head, root.right);
    }

    private boolean dfs(ListNode head, TreeNode root) {
        if (head == null) return true;
        if (root == null) return false;
        return head.val == root.val && (dfs(head.next, root.left) || dfs(head.next, root.right));
    }

Source: https://leetcode.com/problems/linked-list-in-binary-tree/discuss/524881/Python-Recursive-Solution-O(N)-Time

Python:

    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        DELIMITER = '|'
        subpath = ''
        while head:
            subpath += str(head.val) + DELIMITER
            head = head.next
    
        def dfs(root, path):
            if subpath in path:
                return True
            if not root:
                return False
            return dfs(root.left, path+str(root.val)+DELIMITER) or dfs(root.right, path+str(root.val)+DELIMITER)
            
        return dfs(root, "")

Source: https://leetcode.com/problems/linked-list-in-binary-tree/discuss/524852/Python-DFS
"""
