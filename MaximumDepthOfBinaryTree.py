# 1 levelOrder 방법으로 풀 수 있을 것
from collections import deque

def bfs(root):
    visited = []
    if root is None:
        return 0
    
    q = deque()
    q.append((root, 1))
    
    max_depth = 0
    while q:
        cur_node, depth = q.popleft()
        max_depth = max(max_depth, depth)

        if cur_node.left:
            q.append((cur_node.left, depth+1))
        if cur_node.right:
            q.append((cur_node.right, depth+1))
    return max_depth

class TreeNode:
    def __init__(self, l=None, r=None, v=0):
        self.left = l
        self.right = r
        self.value = v

root = TreeNode(v=3)
root.left = TreeNode(v=9)
root.right = TreeNode(v=20)
root.right.left = TreeNode(v=15)
root.right.right = TreeNode(v=7)

print(bfs(root))

# postorder로도 문제를 해결할 수 있다

def dfs(root):
    if root is None:
        return 0

    left = dfs(root.left)
    right = dfs(root.right)

    max_depth = max(left, right) + 1

    return max_depth

print(dfs(root))


