# [Problem](https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/)

# Intuition
This problem resembles a tree traversal combined with a breadth-first search (BFS) on an undirected graph. Given the tree structure and the unique value of each node, the immediate intuition is to convert the binary tree into a graph representation, as BFS is naturally suited for problems involving the shortest path or minimum time to reach all nodes in a graph.

# Approach
1. Convert Tree to Graph: Since the binary tree nodes have unique values, use these values as keys in an adjacency list to represent the graph. Traverse the binary tree and for each node, add its children and parent (if present) to its adjacency list. This step effectively transforms the tree into an undirected graph.

2. Breadth-First Search (BFS): Start a BFS from the node start. The BFS will propagate the infection to adjacent nodes. Keep track of each node's infection time (minutes passed) and use a visited set to prevent revisiting nodes.

3. Determine Maximum Infection Time: As BFS progresses, update the maximum time taken to infect a node. This value represents the total time required to infect the entire tree.

# Complexity
Time complexity: $O(n)$ The entire tree is traversed once to build the graph, and BFS traverses each node once. n is the number of nodes in the tree.
Space complexity: $O(n)$ The graph representation and BFS queue may hold all nodes in the worst case.

# Code
```python
# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        def build_graph(node: TreeNode, parent=None):
            """
            We recursively transform a tree into an undirected graph by performing
            a recursive depth first search. We utilize the assumption that each node
            in the tree has a unique value, then our algorithm consists of:

                - initialize adjacency list
                - add parent node value to adjacency list (forall nodes except the root)
                - perform recursive step on children nodes
            """
            graph[node.val] = []
            if parent:
                graph[node.val].append(parent.val)
            if node.left:
                graph[node.val].append(node.left.val)
                build_graph(node.left, node)
            if node.right:
                graph[node.val].append(node.right.val)
                build_graph(node.right, node)
        
        graph = {}
        build_graph(root)

        # Perform a breadth-first search for the depth of the tree
        # starting at graph[start]. (Using assumption that start is in the tree)

        queue = deque([(start, 0)]) # [(node value, time infected)]
        visited = set()
        max_time = 0

        while queue:
            val, time = queue.popleft()
            if val not in visited:
                visited.add(val)
                max_time = max(time, max_time)
                for adj_val in graph[val]:
                    if adj_val not in visited:
                        queue.append((adj_val, time + 1))
        return max_time
```