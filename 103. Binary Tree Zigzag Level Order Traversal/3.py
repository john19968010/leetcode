class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        need_reverse = False
        temp_queue, next_queue = [root], []
        temp_values, ret_values = [], []
        while True:
            if len(temp_queue) <= 0:
                if need_reverse:
                    temp_values = temp_values[::-1]
                ret_values.append(temp_values)
                temp_values = []

                if len(next_queue) == 0:
                    return ret_values
                else:
                    need_reverse = need_reverse == False
                    temp_queue = next_queue
                    next_queue = []

            root = temp_queue.pop(0)
            value, left, right = root.val, root.left, root.right
            temp_values.append(value)
            if left is not None:
                next_queue.append(left)
            if right is not None:
                next_queue.append(right)


a = Solution().zigzagLevelOrder(root)
print(a)
