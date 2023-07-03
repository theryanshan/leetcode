# Tip: for easy calculation, we set the depth of null node to be -1, and the depth of leaf node to be 0. The diameter of a node is the sum of the depth of its left and right child + 2.


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            diameter[0] = max(diameter[0], left + right + 2)
            return max(left, right) + 1

        diameter = [0]
        dfs(root)
        return diameter[0]
