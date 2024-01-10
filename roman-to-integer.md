# [Problem](https://leetcode.com/problems/roman-to-integer/description/)

# Intuition
The problem of converting a Roman numeral to an integer is based on the principle of subtracting the value of a symbol if the next symbol is of greater value. This naturally suggests the use of a pointer to keep track of the current symbol, and a variable to keep track of the result. When iterating through the string, we check if the next symbol is of greater value. If it is, we subtract the current symbol from the result. Otherwise, we add the current symbol to the result. Additionally, we know that the last symbol in the string will always be added to the result, so we can use this as a stopping condition. 

# Complexities
- Time Complexity: $O(n)$, where $n$ is the length of the input string.
- Space Complexity: $O(1)$, constant space is used.

# Code
This solution beat 95% of other submissions' runtime.

```
class Solution:
    def romanToInt(self, s: str) -> int:
        value = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        symbols = [c for c in s]
        len_s = len(s)
        result = 0
        
        for ind, symbol in enumerate(symbols):
            
            if ind + 1 == len_s: # terminal condition
                result += value[symbol]
                return result

            next_symbol = symbols[ind + 1]

            if value[next_symbol] > value[symbol]:
                # subtract from result
                result -= value[symbol]

            else:
                result += value[symbol]
```