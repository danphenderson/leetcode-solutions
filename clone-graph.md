# [Problem](https://leetcode.com/problems/clone-graph/)

# Intuition
The challenge is to create a clone of the given graph where each node in the new graph is a copy of the nodes in the original graph, including their connections.

Understanding the Problem:
    **Input**: The input is a reference to a node in a connected, undirected graph.
    **Output**: The output should be a deep copy of the graph, i.e. each node in the new graph should be a new object with the same value as the corresponding node in the original graph. The connections (edges) should also be replicated by updating the nodes adjacency list.

# Approach

Iterative or recursive algorithm:
    **Depth-First Search (DFS) or Breadth-First Search (BFS)**: Both DFS and BFS can be used for this problem. You traverse the graph starting from the given node, and for each node, you create a copy.
    **Hash Map**: Use a hash map to store the mapping between the original nodes and their copies. This helps in avoiding creating multiple copies of the same node and also helps in connecting the nodes in the new graph.


# Complexities
- Time Complexity: $O(V + E)$, where $V$ is the number of vertices (nodes) and $E$ is the number of edges in the graph.
- Space Complexity: $O(V)$ for the hash map. Additionally, the stack (or recursion stack) can also take up to $O(V)$ space in the worst case. Therefore, the total space complexity is $O(V)$.

# Code
Recursive solution using DFS:

```python
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        def dfs(old_node):
            if old_node in clone_map:
                return clone_map[old_node]
            
            # Clone the node
            new_node = Node(old_node.val)
            clone_map[old_node] = new_node

            # Clone the neighbors
            for neighbor in old_node.neighbors:
                new_node.neighbors.append(dfs(neighbor))
            
            return new_node

        clone_map = {}
        return dfs(node)           
```

Iterative solution using DFS:

```python
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clone_map = {node: Node(node.val)}
        stack = [node]

        while stack:
            old_node = stack.pop()

            for neighbor in old_node.neighbors:
                if neighbor not in clone_map:
                    # Clone the neighbor and add it to the map
                    clone_map[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                
                # Link the clone
                clone_map[old_node].neighbors.append(clone_map[neighbor])

        return clone_map[node]
```