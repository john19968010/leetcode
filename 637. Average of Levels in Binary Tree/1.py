# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


def averageOfLevels(root):
    if root is None:
        return []

    ret, queue = [], [root]
    temp_values, temp_queues = [], []
    while queue:
        temp_root = queue.pop(0)
        temp_values.append(temp_root.val)
        left_root, right_root = temp_root.left, temp_root.right
        if left_root is not None:
            temp_queues.append(left_root)
        if right_root is not None:
            temp_queues.append(right_root)

        if not queue:
            avr_value = float("{:.5f}".format(sum(temp_values) / len(temp_values)))
            ret.append(avr_value)
            print(ret)
            queue = temp_queues
            temp_values, temp_queues = [], []

    return ret


print(averageOfLevels(root))
