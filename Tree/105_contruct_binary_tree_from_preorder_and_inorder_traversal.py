# Time: O(n)
# Space: O(n), worse case O(n) for skewed tree, average case O(logn) for balanced tree
# Tip: every node in preorder is a root of a subtree of inoder, so we can use preorder to find the root of the tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    rootIdx = 0

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def recursive(left, right):
            if left > right:
                return
            rootVal = preorder[self.rootIdx]
            root = TreeNode(rootVal)
            self.rootIdx += 1
            inorderMidIdx = inorder.index(rootVal)

            root.left = recursive(left, inorderMidIdx - 1)
            root.right = recursive(inorderMidIdx + 1, right)

            return root

        idxMap = {}
        for idx, val in enumerate(inorder):
            idxMap[val] = idx

        return recursive(0, len(inorder) - 1)
