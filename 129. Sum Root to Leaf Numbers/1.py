# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = 0

    def sum_numbers(self, root: TreeNode) -> int:
        self.pre_order_travel_helper(root, "")
        return self.ans

    def pre_order_travel_helper(self, node, val: str):
        if node is None:
            return ""

        val += str(node.val)
        if node.left is None and node.right is None:
            self.ans += int(val)

        self.pre_order_travel_helper(node.left, val)
        self.pre_order_travel_helper(node.right, val)
