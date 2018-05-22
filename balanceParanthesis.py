import sys
import collections

hashmap = {
    ')': '(',
    '}': '{',
    ']': '['
}

def isBalanced(s):
    # Complete this function
    if not s:
        return "YES"
    stack = collections.deque()
    for char in s:
        if char in '{[(':
            stack.appendleft(char)
        elif char in '}])':
            if len(stack) == 0:
                return "NO"
            elem = stack.popleft()
            if char not in hashmap.keys() or elem != hashmap[char]:
                return "NO"
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"
