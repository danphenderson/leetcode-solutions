# [Problem](https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/)

# Intuition

In the context of a DAG, a node $a$ is an ancestor of a node $b$ if and only if there is a
directed path from $a$ to $b$.

My initial thought was to locate the maximum and minimum values in the tree using a simple depth first search, then return the absolute difference of the maximum and minimum values.
However, this implementation wouldn't take into account the case where the maximum and minimum nodes are not ancestors. To solve this problem, we must maintain maximum and minimum values encountered along the path from the root to the current node, effectively ensuring
that only ancestor-descendant pairs are considered in a recursive call stack.


# Approach
1. **Pass Maximum and Minimum Values**: In the DFS function, pass the maximum and minimum values found so far in the current path. This means each recursive call carries the range of values from its ancestors.

2. **Calculate Difference at Each Node**: At each node, calculate the difference between the current node's value and the maximum/minimum values passed down. This will ensure you're only considering ancestor-descendant pairs.

3. **Update the Maximum Difference**: Keep a global or class-level variable to maintain the maximum difference found so far and update it if a larger difference is found.

4. **Recursively Call for Children**: When calling DFS for the children nodes, update the maximum and minimum values accordingly.

# Complexities
Let $n$ be the number of nodes in the tree.

- Time Complexity: $O(n)$, as we perform a DFS with a constant amount of work at each node.
- Space Complexity: is mainly dictated by the depth of the recursion stack, which in turn depends on the height of the tree. In the event that the tree is skewed, our recursion depth would $n$, i.e. the space complexity is $O(n)$



# Code
Below is the recursive implementation, as disscussed above.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curr_max, curr_min):
            if not node: 
                return curr_max - curr_min

            # Perform maximum and minimum updates
            curr_max = max(curr_max, node.val)
            curr_min = min(curr_min, node.val)

            # Recursively step into children nodes
            left = dfs(node.left, curr_max, curr_min)
            right = dfs(node.right, curr_max, curr_min)

            # Return the maximum difference found in either subtree
            return max(left, right)
             
        return dfs(root, root.val, root.val)
```

For practice, I implemented an iterative DFS as I was curious to see how it effected my
performance. In practice, recursion is generally more eligant but slightly less performant.

The iterative solution above beat 98.23% and 96.12% percent of Python3 users in runtime and memory, respectively.

```python
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_diff = 0
        stack = [(root, root.val, root.val)]

        while stack:
            node, current_max, current_min = stack.pop()

            if not node:
                continue

            current_diff = max(abs(node.val - current_max), abs(node.val - current_min))
            max_diff = max(max_diff, current_diff)

            new_max = max(current_max, node.val)
            new_min = min(current_min, node.val)

            if node.left:
                stack.append((node.left, new_max, new_min))
            if node.right:
                stack.append((node.right, new_max, new_min))

        return max_diff
```

