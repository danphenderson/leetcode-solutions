# [Problem](https://leetcode.com/problems/longest-common-prefix/description/)

# Intuition
The problem of finding the longest common prefix is based on the principle of matching characters in the same position in each string. This naturally suggests the use of a pointer to keep track of the current position in each string. Additonally, we know the prefix cannot be longer than the shortest string, so we can use the length of the shortest string as a stopping condition.

# Complexities
- Time Complexity: $O(n)$, where $n$ is the length of the shortest string.
- Space Complexity: $O(1)$, constant space is used.


# Code
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        min_length = min(len(word) for word in strs)

        longest_common_prefix = ""

        for ind in range(min_length):
            current_char = strs[0][ind]
            if all(s[ind] == current_char for s in strs):
                longest_common_prefix += current_char
            else:
                break # mismatch found
            
        return longest_common_prefix
```