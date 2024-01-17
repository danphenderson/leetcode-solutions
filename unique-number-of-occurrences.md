# [Problem](https://leetcode.com/problems/unique-number-of-occurrences/)

# Approach
We define the multiset/bag by using the `Counter` object from the standard `collections` module. Next, we iterate over each frequencey in the bag, keeping track of frequencies that we have already seen; if we encounter a frequency that is already seen, we return `False`.
Otherwise, no two elements in the input `arr` have the same number of occurences and we return `True`.

# Complexities
- Time Complexity: The time complexity is $O(n)$, where $n$ is the number of elements in the array. This complexity arises because we iterate through each element of the array once to build the Counter (bag), and then we iterate through the values of the bag, which is at most n.

- Space Complexity: The space complexity is $O(n)$. This is due to the space required for the Counter object and the set unique_freqs. In the worst-case scenario, if all elements in the array are unique, the Counter object will store $n$ key-value pairs, and the set will also potentially store $n$ unique frequencies.

# Code
```python
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        bag = Counter(arr)
        unique_freqs = set()
        for freq in bag.values():
            if freq in unique_freqs:
                return False
            unique_freqs.add(freq)
        return True
```