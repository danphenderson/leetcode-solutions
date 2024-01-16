# [Problem](https://leetcode.com/problems/insert-delete-getrandom-o1)

# Intuition
This is a simple task; I am confused why it of medium difficulty.


# Code

```python
from random import randrange

class RandomizedSet:

    def __init__(self):
        self._set = set()

    def insert(self, val: int) -> bool:
        if val in self._set:
            return False
        self._set.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self._set:
            return False
        self._set.remove(val)
        return True


    def getRandom(self) -> int:
        return list(self._set)[randrange(len(self._set))]
```
