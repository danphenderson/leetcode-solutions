# [Problem](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string)

# Approach

The brute-force approach to solving this problem involves checking every possible starting position of the needle within the haystack. We iterate through the haystack, and for each position, we check if the substring of the haystack starting from that position and having the same length as the needle matches the needle. The first such position where a match occurs is returned. If no such position is found, we return -1.

This approach is straightforward and does not require any preprocessing or advanced algorithms. However, it can be less efficient for large strings because it potentially requires a comparison of every substring of the haystack with the needle.

# Code

```python
def strStr(haystack, needle):
    # Edge case: if needle is empty
    if not needle:
        return 0

    len_haystack, len_needle = len(haystack), len(needle)

    # Iterate through the haystack
    for i in range(len_haystack - len_needle + 1):
        # Check if the substring matches the needle
        if haystack[i:i + len_needle] == needle:
            return i

    # Needle is not found in haystack
    return -1
```

# Complexities
- Time Complexity: The time complexity is $O(n*m)$, where $n$ is the length of the haystack and $m$ is the length of the needle. This is because, in the worst case, we might need to check each substring of the haystack against the needle, and each such check takes $O(m)$ time.

- Space Complexity: The space complexity is $O(1)$. We only use a few extra variables for the indices and lengths of the strings.