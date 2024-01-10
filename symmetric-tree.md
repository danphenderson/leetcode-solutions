# [Problem](https://leetcode.com/problems/symmetric-tree/description/)

# Intuition
The key to solving this problem lies in understanding the definition of a symmetric tree. A tree is symmetric if its left and right subtrees are mirror images of each other. This means that each node in the left subtree has a corresponding node in the right subtree with the same value, and their children mirror each other as well. We can use a recursive approach to compare corresponding nodes in each subtree.

# Approach
We implement a helper function `is_mirror` that takes two nodes as arguments, it returns True if the two nodes are mirrors of each other, otherwise, it returns `False`. The function `is_mirror` checks the following conditions:

If both nodes are None, the trees are mirrors by definition (empty trees).
If one node is None and the other is not, the trees are not mirrors.
If the values of the nodes are different, the trees are not mirrors.
If none of these conditions are met, we recursively check:
If the left child of the left node is a mirror of the right child of the right node.
If the right child of the left node is a mirror of the left child of the right node.

The main function `isSymmetric`` initially calls `is_mirror`` with the left and right children of the root node.

# Complexity
- Time complexity: The time complexity is $O(n)$, where nnn is the number of nodes in the tree. This is because we visit each node once.

- Space complexity: The space complexity is $O(h)$, where $h$ is the height of the tree. This space is used by the call stack during the recursion. In the worst case (a completely unbalanced tree), this could be $O(n)$


# Code
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        def is_mirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            # Otherwise, perform recursive step
            return (left.val == right.val) and is_mirror(left.left, right.right) and is_mirror(left.right, right.left)
        
        return is_mirror(root.left, root.right)
```