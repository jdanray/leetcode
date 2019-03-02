// https://leetcode.com/problems/maximum-binary-tree-ii/

class Solution {
	public TreeNode insertIntoMaxTree(TreeNode root, int val) {
		if (root == null || val > root.val) {
			TreeNode newroot = new TreeNode(val);
			newroot.left = root;
			return newroot;
		}
		
		root.right = insertIntoMaxTree(root.right, val);
		return root;
	}
}
