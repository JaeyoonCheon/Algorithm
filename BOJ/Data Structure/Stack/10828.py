"""
10828번 스택

1.  단순 스택 구현
"""

import sys
import collections

stack = collections.deque()

N = int(input())

for _ in range(N):
    operation = sys.stdin.readline().split()

    if operation[0] == "push":
        stack.append(operation[1])
    elif operation[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print("-1")
    elif operation[0] == "size":
        print(len(stack))
    elif operation[0] == "empty":
        if stack:
            print("0")
        else:
            print("1")
    else:
        if stack:
            print(stack[len(stack) - 1])
        else:
            print("-1")
