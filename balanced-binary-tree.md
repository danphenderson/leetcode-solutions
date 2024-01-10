# [Problem](https://leetcode.com/problems/balanced-binary-tree/description/)

# Intuition
To determine if a binary tree is height-balanced, you need to ensure that for every node in the tree, the height of the two subtrees of that node differ by no more than one. A height-balanced tree is often referred to as a balanced binary tree.

# Approach
Here's a step-by-step approach to solve this problem:

1. Define Tree Height: Understand that the height of a node in a binary tree is the number of edges on the longest path from the node to a leaf. A leaf node will have a height of 0.

2. Recursive Height Calculation: Use a recursive function to calculate the height of each node. This function should return the height of a node as an integer.

3. Balance Check at Each Node: At each node, you need to check the balance condition: the absolute difference between the heights of the left subtree and the right subtree should be no more than one.

4. Propagate Imbalance: If any subtree is unbalanced, propagate this information up the tree. This can be done by using a special value (like -1) to indicate that a subtree is unbalanced.

5. Final Decision: After traversing all nodes, if you never encounter an unbalanced subtree, then the tree is height-balanced

# Complexity
Time complexity: $O(n)$, where $n$ is the number of nodes. That is, in the worst case scenario, we visit every node in the BST.

Space complexity: $O(H)$, where $H$ is the depth of the balanced binary subtree. In the event that the result is true, we have a space complexity of $\log{n}$.


# Code
The submitted code beat 99-percent of all Python submissions' runtime.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(node) -> int:
            # Base Case: an empty subtree is balanced with height 0
            if not node:
                return 0

            # Recursively get the height of the left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)

            # If any subtree is unbalanced, propagate the unbalance up
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1

            # Otherwise, return the height of the node
            return max(left_height, right_height) + 1


        return height(root) != -1
```
