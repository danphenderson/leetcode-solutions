# [Problem](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

# Intuition
The problem asks to find the length of the longest substring without repeating characters in a given string s.

The challenge lies in efficiently scanning the string while keeping track of the characters we've seen so far and their positions. A key intuition is to use a sliding window approach, expanding and shrinking the window as we move through the string to maintain a substring without duplicates.

# Approach
We use a hash map, char_map, to store the characters and their most recent indices in the string. This allows us to quickly check if a character is in the current window and to update the window's start position if necessary.

1. Initialize start and max_length to 0. start indicates the beginning of the current window, and max_length keeps track of the maximum length found so far.
2. Iterate through the string using end as the index.
3. If the current character s[end] is found in char_map, it means we've encountered a duplicate. Update start to the maximum of its current value and the next index after the last occurrence of s[end]. This effectively shrinks the window to exclude the repeating character.
4. Update the char_map with the current index of s[end].
5. Update max_length with the larger of its current value and the length of the current window (end - start + 1).
 
The loop continues until we have scanned the entire string, and max_length will contain the length of the longest substring without repeating characters.

# Complexities
- Time Complexity: $O(n)$, where $n$ is the length of the string. We traverse the string once, with constant-time operations in each iteration.
- Space Complexity: $O(min(m, n))$, where $m$ is the size of the character set. The hash map can grow up to the size of the character set (limited by the smaller of m and n).

# Code
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        start = max_length = 0

        for end in range(len(s)):
            if s[end] in char_map:
                start = max(start, char_map[s[end]] + 1)
            char_map[s[end]] = end
            max_length = max(max_length, end - start + 1)

        return max_length
```