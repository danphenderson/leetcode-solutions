# [Problem]()

# Intuition
It involves finding the minimum number of character changes needed to make two strings anagrams of each other. An anagram of a string is another string that contains the same characters, only the order of characters can be different.

# Approach
To solve this problem, we need to compare the frequency of each character in both strings. The minimum number of steps is equal to the total count of characters that are in excess in one string compared to the other.
 
# Complexities
### Time Complexity:
    1. Counting Characters in`s` and `t`: The Counter objects for`s` and `t` are created by iterating over each string once. If `n` is the length of the longer string (s or t), this operation has a time complexity of $O(n)$. The Counter essentially creates a hash map of character frequencies, which is a linear time operation.

    2. Calculating the Difference: The diff = Counter(s) - Counter(t) operation involves iterating over the entries in the Counter objects. In the worst case, this will involve going through all unique characters in`s` and `t`. However, since the number of unique characters (especially if we're considering standard ASCII or Unicode characters) is limited and significantly smaller than n, this can be considered an $O(1)$ operation in terms of the length of the strings.

    3. Summing the Differences: The sum(diff.values()) operation is linear with respect to the number of unique characters in`s` and `t`. Again, due to the limited number of unique characters, this is effectively an $O(1)$ operation in terms of n.

Overall, the time complexity of your function is $O(n)$, where `n` is the length of the longer string.

### Space Complexity:
    1. Storage for Counters: The space complexity is largely influenced by the storage required for the Counter objects. Each Counter stores a frequency count for each unique character in`s` and `t`. The space required for these counters is proportional to the number of unique characters in the strings. Since the number of unique characters is limited and does not grow with n, the space complexity due to the counters is $O(1)$ in terms of the length of the strings.

    2. Storage for diff: The diff object is a Counter that stores the difference in character counts between`s` and `t`. Its size is also proportional to the number of unique characters, which is a constant not dependent on n.

    3. Therefore, the overall space complexity of your function is $O(1)$, as it does not significantly grow with the length of the input strings.


# Code

```python
def min_steps_anagrom(s: str, t: str) -> int:
    from collections import Counter

    # determine the difference between the characters in both strings
    diff = Counter(s) - Counter(t)
    # minimum number of steps to make `t` an anagrom of s
    return sum(diff.values())
```