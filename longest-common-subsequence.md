# [Problem](https://leetcode.com/problems/longest-common-subsequence/description)

# Approach
Below is a step-by-step approach to solve this problem using dynamic programming:

1. Understanding the Subproblem: The key idea is to break down the problem into smaller, more manageable subproblems. We can consider the problem of finding the longest common subsequence of prefixes of the two strings. For any pair of indices `i` and `j`, we consider the longest common subsequence of `text1[0...i]` and `text2[0...j]`.

2. Dynamic Programming Array: We can create a 2D array dp where `dp[i][j]` will store the length of the longest common subsequence of `text1[0...i]` and `text2[0...j]`.

3. Base Case: The base case is when either `i` or `j` is 0, which means one of the strings is empty. In this case, the longest common subsequence is 0.

4. Recursive Relation: For `dp[i][j]`, if `text1[i] == text2[j]`, then the character at index `i` and `j` is part of the longest common subsequence, and we add 1 to the result of `dp[i-1][j-1]`. Otherwise, the character at either `i` or `j` is not part of the longest common subsequence, and we take the maximum of `dp[i-1][j]` and `dp[i][j-1]`.

5. Implementation: We iterate over the lengths of the two strings and fill up the `dp` array according to the recursive relation.

6. Return the Result: The length of the longest common subsequence of text1 and text2 is then `dp[len(text1)][len(text2)]`.

# Complexities
- Time Complexity: $O(mn)$, where $m$ and $n$ are the lengths of the input strings
- Space Complexity: similarly, $O(mn)$.

# Code

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]
```