# [Problem](https://leetcode.com/problems/binary-tree-inorder-traversal/description/)

# Intuition
Inorder traversal of a binary tree is a fundamental concept in tree-based algorithms, primarily used to retrieve elements in a linear, sorted order when dealing with a binary search tree. The essence of this approach lies in the traversal sequence: visit the left subtree, the root node, and then the right subtree. This process ensures that the values are accessed in an ascending manner if the binary tree is a binary search tree. Note, this is an example of a depth-first search.


# Approach
The provided algorithm employs a recursive strategy to achieve inorder traversal. It defines an auxiliary function, traverse, that accepts a TreeNode and a list, result, which is used to store the traversal outcome. The function adheres to the following steps:

1. Base Case: If the current node is None, return immediately, indicating the end of a branch.
2. Left Subtree: Recursively call traverse on the left child of the current node. This step explores the left subtree entirely before accessing the current node's value.
3. Current Node: Append the current node's value to result, respecting the inorder sequence.
4. Right Subtree: Recursively call traverse on the right child, ensuring all nodes in the right subtree are processed after the current node.

The initial invocation of traverse starts with the root node, triggering a depth-first exploration of the tree in an inorder manner.

# Complexity
- Time Complexity: The time complexity is $$O(n)$$, where $n$ is the number of nodes in the binary tree. This is because each node in the tree is visited exactly once during the traversal process.
- Space Complexity: The space complexity is $$O(h)$$, where $h$ is the height of the tree. This represents the space used by the recursion stack. In the worst case (a skewed tree), the space complexity can degrade to $O(n)$, while for a balanced tree, it remains at $O(logn)$.


# Code
```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def traverse(node, result):
            
            if not node:
                return None
                
            traverse(node.left, result)
            result.append(node.val)
            traverse(node.right, result)
        
        result = []
        traverse(root, result)
        return result
```