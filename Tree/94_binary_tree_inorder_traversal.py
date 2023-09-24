# Time O(n), Space O(n)
# Append left subtree of current node to stack, then pop the stack and append the node value to res, then append right subtree of current node to stack. We only need to set cur to cur.right at the end, because we will append left subtree of cur to stack in the next iteration.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res
