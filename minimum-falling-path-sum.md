# [Problem](https://leetcode.com/problems/minimum-falling-path-sum)

# Intuition
Given the square matrix, we must find the minimum sum of a falling path through the matrix. A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Using a dynamic programming solution, with a bottom-up approach, we can build a table with each entry in a row will store the minimum sum of a falling path ending at that entry.

# Approach
Here are the steps for the algorithm:

1. Initialization: Copy the first row of the matrix to the first row of a DP (Dynamic Programming) matrix, as the first row doesn't have any rows above it.

2. Filling DP Matrix: For each entry in the DP matrix starting from the second row, calculate the minimum sum by considering the current entry value in `matrix` and the minimum of the three entries directly above it (the same column, one column to the left, and one column to the right).

3. Handling Edges: When filling the DP matrix, make sure to handle the first and last columns separately, as they don't have three entries above them.

4. Finding the Result: The answer will be the minimum value in the last row of the DP matrix.


# Complexities
- Time Complexity: $O(n^2)$
- Space Complexity: $O(n^2)$

# Code

The solution below beat 99% of other submissions' runtime.

```python
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # Initialize space
        n = len(matrix[0])
        dp = [[0] * n for _ in range(n)]

        # Set the first row of DP from first row of the matrix
        dp[0][:] = matrix[0][:]

        # Fill in the DP
        for i in range(1, n):
            for j in range(n):
                left = dp[i-1][j-1] if j > 0 else float('inf')
                right = dp[i-1][j+1] if j < n - 1 else float('inf')
                dp[i][j] = matrix[i][j] + min(dp[i-1][j], left, right)

        # Return the minimum in the last row                 
        return min(dp[-1])
```