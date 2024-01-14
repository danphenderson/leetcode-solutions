
# [Problem](https://leetcode.com/problems/determine-if-two-strings-are-close)

# Intuition
*Definition*: Stings $w_1$ and $w_2$ are **close** if you can attain one string from the other applying the following operations:
- reordering of the characters.
- swapping the frequency of two characters occurence in the string.

It suffices to examine the multiset of $w_1$ and $w_2$ to build out the algorithm.

# Approach
To determine if `word1` and `word2` are close we take the following steps:

1. Length Check: First, check if the lengths of word1 and word2 are different. If they are, it's impossible for the strings to be close, so return False immediately. This optimization avoid's unnecessary computation.

2. Frequency Count: Use `Counter` from `collections` to get the frequency of each character in both words. The Counter object essentially creates a dictionary where the keys are characters, and the values are the number of times those characters appear in the string.

3. Character Sets: Convert the keys of both `Counter` objects (which are the unique characters in each word) into sets. This is used to check if both strings contain the exact same characters.

4. Frequency Lists: Convert the values of the `Counter` objects (which are the frequencies of each character) into lists and then sort these lists inplace. This step is important because, while the frequency of each character can be transformed into the frequency of another character, the overall multiset of frequencies must remain the same for the strings to be close.

5. Determine Result: Compare both the character sets and the sorted frequency lists. If both the sets of characters and the sets of frequencies are equal for both strings, then the strings are close according to the problem's definition. Otherwise, they are not.

# Complexities
- Time Complexity: $O(n)$, where n is the length of the longer input string.
- Space Complexity: $O(1)$, as the space used does not scale with the size of the input.

# Code

```python
from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Early exit condition
        if len(word1) != len(word2):
            return False

        w1_bag, w2_bag = Counter(word1), Counter(word2)

        
        w1_chars, w2_chars = set(w1_bag.keys()), set(w2_bag.keys())
        w1_freqs, w2_freqs = list(w1_bag.values()), list(w2_bag.values())

        w1_freqs.sort()
        w2_freqs.sort()

        # Determine if two strings are close
        if w1_chars == w2_chars and w1_freqs == w2_freqs:
            return True
        return False
```

