# [Problem](https://leetcode.com/problems/minimum-depth-of-binary-tree/description/)

# Intuition
The objective is to find the shortest path from the root to the nearest leaf node in a binary tree. A leaf is a node with no children. Since we're interested in the shortest path to a leaf, a breadth-first search (BFS) is an ideal strategy. BFS explores the tree level by level, guaranteeing that the first leaf node encountered is the closest to the root.

# Approach
To implement BFS, we use a queue to hold each tree node along with its depth level. We start from the root node (depth 1) and process nodes level by level. For each node, we check if it's a leaf (no left and right children). If it's a leaf, we return its depth as the minimum depth. If not, we add its non-null children to the queue with their corresponding depth levels incremented by 1. This process continues until we find the first leaf node.

# Complexity
- Time complexity: The time complexity is $O(n)$, where $n$ is the number of nodes in the tree. In the worst case, we might have to visit all nodes once.

- Space complexity: The space complexity is also $O(n)$ in the worst case. This happens when the tree is extremely unbalanced (e.g., every node only has one child), and all nodes end up in the queue before we find the first leaf.

# Code
```python
from collections import deque as _deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Check for early exit
        if not root:
            return 0
        
        # Queue holds pairs of (node, depth)
        queue = _deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()

            # Check if we have found a leaf node
            if not node.left and not node.right:
                return depth

            # Otherwise, enqueue the node's children
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
```

This solution beat $95$-percent of all Python submissions on LeetCode. 