# https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        order = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            order = [node.val] + order
            for child in node.children:
                stack.append(child)
        return order
