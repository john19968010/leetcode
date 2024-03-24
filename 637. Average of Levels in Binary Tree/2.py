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


def averageOfLevels(root: TreeNode | None) -> list[float]:
    ret, queue = [], [root]
    while queue:
        level_values, level_length = [], len(queue)

        for i in range(level_length):
            temp_root = queue.pop(0)
            if temp_root:
                level_values.append(temp_root.val)
                queue.append(temp_root.left)
                queue.append(temp_root.right)

        if level_values:
            avr_value = float("{:.5f}".format(sum(level_values) / len(level_values)))
            ret.append(avr_value)

    return ret


print(averageOfLevels(root))
