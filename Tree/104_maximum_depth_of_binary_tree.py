# Time: O(n)
# Space: O(height)
# Tip: traverse the tree, at current level return the max of left and right child's depth + 1. The base case is when the node is None, return 0.


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1


# Interative BFS solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        level = 0
        while queue:
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            level += 1
        return level


# Interative preorder DFS solution
# Tip: pop the stack, push the right then left child into the stack for preorder traversal.
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_level = 1
        stack = [[root, 1]]
        while stack:
            cur, level = stack.pop()
            max_level = max(max_level, level)
            if cur.left:
                stack.append([cur.left, level + 1])
            if cur.right:
                stack.append([cur.right, level + 1])
        return max_level
