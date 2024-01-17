# [Problem](https://leetcode.com/problems/reverse-integer/description/)

# Approach
The problem requires reversing the digits of a given 32-bit signed integer and returning 0 if the reversed integer overflows. The solution involves the following steps:

Absolute Value and String Conversion: Convert the absolute value of the given integer to a string to facilitate the reversal of digits.
Reversal: Reverse the string and convert it back to an integer.
Range Check: Verify if the reversed integer fits within the 32-bit signed integer range. If it overflows, return 0.
Sign Adjustment: Adjust the sign of the reversed integer to match the original integer's sign.
This approach efficiently reverses the integer while handling the edge cases associated with 32-bit integer limits.

# Complexities
- Time Complexity: The solution has a time complexity of $O(n)$, where $n$ is the number of digits in the integer. This is because each digit is processed once during the reversal process.
- Space Complexity: The space complexity is $O(1)$, as the solution uses a fixed amount of extra space regardless of the input size.

# Code

```python
class Solution:
    def reverse(self, x: int) -> int:
        x_mag_reversed = int(str(abs(x))[::-1])
        limit = 2**31
        if x < 0 and x_mag_reversed <= limit:
            return - x_mag_reversed
        if x > 0 and x_mag_reversed < limit:
            return x_mag_reversed
        return 0
```

Note, my solution above violates the assumption that our environment does not allow us to store 64-int's.

To account for our assumption, a proper solution would look like this:

def reverse(x: int) -> int:
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    
    sign = -1 if x < 0 else 1
    x = abs(x)
    reversed_x = 0
    
    while x != 0:
        pop = x % 10
        x //= 10
        
        # Check for overflow
        if reversed_x > INT_MAX // 10 or (reversed_x == INT_MAX // 10 and pop > INT_MAX % 10):
            return 0
        
        reversed_x = reversed_x * 10 + pop
    
    return sign * reversed_x

However, or modified version also violates the assumption for x=-2**31, namely, such `x` will overflow when executing `x=abs(x)` in a 32-bit environment. This is a rather odd question to consider in the Python programming language.