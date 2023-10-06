from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bfs(self, root):
    queue = deque()

    if root:
        queue.append(root)

    level = 0

    while len(queue):
        print("level: ", level)
        for i in range(len(queue)):
            cur = queue.popLeft()
            print(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        level += 1
