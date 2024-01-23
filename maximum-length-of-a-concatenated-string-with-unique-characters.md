# [Problem](https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description)


# Approach
The problem asks for the maximum length of a concatenated string formed by combining strings from the given list, such that the concatenated string contains only unique characters.

The solution uses backtracking to explore all possible combinations of strings. The `backtrack` function is defined with two parameters: `index`, which keeps track of the current position in the `arr` list, and `current_string`, which represents the concatenated string formed so far.

The function first checks if `current_string` contains unique characters by comparing the length of `current_string` with the length of the set of characters in `current_string`. If they don't match, the function returns 0, as it means there's a duplicate character.

If `current_string` is unique, the function iterates through the remaining strings in the `arr`ay starting from the current `index`. For each string, it recursively calls `backtrack`, adding the current string from `arr` to `current_string`. The maximum length is updated accordingly.

This approach systematically explores all combinations, ensuring that each combination is checked for uniqueness before considering its length.


# Complexities
- Time Complexity: $O(2^N * K)$, where $N$ is the number of strings in the array and $K$ is the average length of the strings. This complexity arises because, in the worst case, the algorithm explores all $2^N$ possible combinations of strings, and for each combination, it takes $O(K)$ time to check for unique characters and calculate the length.
- Space Complexity: $O(N * K)$, which is the maximum depth of the recursion stack multiplied by the length of the `current_string`. In the worst case, the recursion goes $N$ levels deep, and the length of the `current_string` could be up to $K$ at each level of recursion.


# Code
```python
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def backtrack(index, current_string):
            unique_length = len(set(current_string))
            if unique_length != len(current_string):
                return 0

            max_length = len(current_string)
            for i in range(index, len(arr)):
                max_length = max(max_length, backtrack(i + 1, current_string + arr[i]))
            
            return max_length

        return backtrack(0, "")
```