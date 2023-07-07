# Time: O(s * t)
# Space: O(height of s)
# tip: for every node in s, check if it's the same tree as t


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:  # empty tree is a subtree of any tree
            return True
        if not s:  # given t is not empty
            return False
        if self.sameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def sameTree(self, s: TreeNode, t: TreeNode):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)


# Solution 2:
# use iterative to traverse the root tree, for every node, if the value is same as subRoot value, check if it's the same tree
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root, sub):
            if not root and not sub:
                return True
            if not root or not sub:
                return False
            if root.val != sub.val:
                return False
            return sameTree(root.left, sub.left) and sameTree(root.right, sub.right)

        stack = [root]
        while stack:
            cur = stack.pop()
            if cur.val == subRoot.val and sameTree(cur, subRoot):
                return True
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return False
