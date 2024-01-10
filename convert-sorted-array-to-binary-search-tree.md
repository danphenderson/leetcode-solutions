# [Problem](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/)

# Complexity
- Time complexity: $O(n)$, where $n$ is the number of nodes. That is, in the worst case scenario, we visit every node in the BST.
- Space Complexity: $O(\log{n})$ (tree is balanced)

# Code
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Base case
        if not nums:
            return
        # Determine the index of the root node in the bst construction
        mid = len(nums) // 2
        root = TreeNode(val=nums[mid])
        # Left substree is built from elements before mid index
        root.left = self.sortedArrayToBST(nums[:mid])
        # Right subtree is built from elements after mid index
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
```