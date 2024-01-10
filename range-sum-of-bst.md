# [Problem](https://leetcode.com/problems/range-sum-of-bst/description/)

# Intuition
Simply search the BST and increment a shared variable to keep track of the sum.

# Approach
Recursively perform an inorder traversal of the BST, starting from the root node. Note, an inorder traversal is simply a depth first search.

My implementation follows this pattern:
- It starts at the root.
- It first tries to go as deep as possible into the left subtree (if the node's value is greater than low).
- After exploring the left subtree, it processes the current node (if the node's value is within the range) by adding it's value to a shared sum.
- Finally, it goes as deep as possible into the right subtree (if the node's value is less than high).
This process is repeated recursively, which is characteristic of DFS.

# Complexity
Time complexity: $O(n)$, where $n$ is the number of nodes in the BST.
Space complexity: $O(n)$, where $n$ is the number of nodes in the BST.

# Code
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        current_sum = 0

        def inorder_traversal(node: TreeNode):
            # terminal condition
            if not node: 
                return
            
            # traverse left subtree if it might contain values within the range
            if node.val > low:
                inorder_traversal(node.left)
            
            # check if current node value is within the range
            if low <= node.val <= high:
                nonlocal current_sum
                current_sum += node.val
            
            # traverse right subtree if it might contain values within the range
            if node.val < high:
                inorder_traversal(node.right)


        inorder_traversal(root)
        
        return current_sum
```