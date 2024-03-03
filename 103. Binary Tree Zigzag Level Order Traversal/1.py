class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.value_list = []
        self.result_list = []

    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        self.get_values(root)
        self.separate_value_list(self.value_list, 1, is_odd=False)
        return self.result_list

    def get_values(self, root: TreeNode | None) -> None:
        if root is None:
            return
        value, left, right = root.val, root.left, root.right
        self.value_list.append(value)
        self.get_values(left)
        self.get_values(right)

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
