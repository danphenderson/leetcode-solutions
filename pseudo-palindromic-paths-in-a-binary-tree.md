# [Problem](https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree)

# Approach
We can solve this problem using Depth First Search (DFS) with a bit mask to keep track of the counts of each digit (value at each node).

1. DFS Traversal: We traverse the tree from the root to each leaf.
2. Bit Mask: We use an integer as a bit mask where the i-th bit represents the count of the digit 'i' in the path. We toggle the i-th bit every time we encounter the digit 'i'.
3. Checking for Pseudo-Palindrome: At each leaf node, we check if the bit mask has at most one bit set. This is equivalent to checking if there is at most one digit with an odd count.

The algorithm is as follows:
1. Initialize a counter for the number of pseudo-palindromic paths.
2. Start DFS from the root node with an initial bit mask of 0.
3. In the DFS function:
    - Toggle the bit corresponding to the current node's value in the bit mask.
    - If it's a leaf node, check if the bit mask has at most one bit set. If yes, increment the counter.
    - Recursively call DFS for the left and right children with the updated bit mask.
4. Return the counter.


# Complexities
- Time Complexity: $O(N)$, where $N$ is the number of nodes in the binary tree. This is because your solution involves a depth-first search (DFS) traversal of the entire tree. Each node in the tree is visited exactly once during the traversal. The operations performed at each node, such as toggling bits and checking for pseudo-palindromes, are executed in constant time.
- Space Complexity: $O(H)$, where $H$ is the height of the binary tree. This space is used by the call stack due to the recursive nature of the DFS. In the worst-case scenario, where the binary tree is highly unbalanced (e.g., a linked list), the height of the tree, and thus the maximum depth of the call stack, becomes $O(N)$. In a balanced tree, this would be $O(log N)$.



# Code

The solution below beats 100.00% of users with Python3 for runtime and memory usage.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def dfs(node, path):
            if not node:
                return 0
            
            # Toggle the bit for the current node's value
            path ^= 1 << node.val

            # Leaf node
            if not node.left and not node.right:
                # Check if path has at most one bit set
                return int(path & (path - 1) == 0)

            # Continue DFS
            return dfs(node.left, path) + dfs(node.right, path)

        return dfs(root, 0)
```