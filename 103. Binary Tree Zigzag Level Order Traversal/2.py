class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.left.left = TreeNode(5)


class Solution:
    def __init__(self):
        self.temp_queue = []
        self.value_list = []
        self.result_list = []

    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        self.temp_queue.append(root)
        self.get_value_by_bft()
        # print(self.value_list)
        self.separate_value_list(self.value_list, 1, is_odd=False)
        return self.result_list

    def get_value_by_bft(self) -> None:
        while len(self.temp_queue) > 0:
            root = self.temp_queue.pop(0)
            if root is None:
                self.value_list.append(None)
                continue
            value, left, right = root.val, root.left, root.right
            self.value_list.append(value)
            if left is not None or right is not None:
                self.temp_queue.append(left)
                self.temp_queue.append(right)

    def separate_value_list(
        self, copy_value_list: list[int], length: int, *, is_odd: bool
    ) -> None:
        if not copy_value_list:
            return
        element_value_list, rest_copy_value_list = (
            copy_value_list[:length],
            copy_value_list[length:],
        )

        if is_odd:
            element_value_list = element_value_list[::-1]

        element_list = [i for i in element_value_list if i is not None]

        self.result_list.append(element_list)
        self.separate_value_list(
            rest_copy_value_list, length * 2, is_odd=is_odd is False
        )


a = Solution().zigzagLevelOrder(root)
print(a)
