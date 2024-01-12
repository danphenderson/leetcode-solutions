# [Problem](https://leetcode.com/problems/determine-if-string-halves-are-alike/)

# Intuition
Solution is to iterate once over the string and keep a count of the vowels found in the left half and the right half.


# Complexities
- Time Complexity: $O(n)$
- Space Complexity: $O(1)$


# Code

```python
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        lc, rc = 0, 0
        is_vowel = lambda c : True if c in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'} else False
        for pos in range(len(s)//2):
            if is_vowel(s[pos]):
                lc += 1
            if is_vowel(s[-pos-1]):
                rc += 1
        return rc == lc
```