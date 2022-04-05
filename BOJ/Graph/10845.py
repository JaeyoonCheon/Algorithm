"""
10845번 큐

1. 큐의 간단한 구현
"""

N = int(input())

q = []

operation = [list(input().split()) for _ in range(N)]

for i in operation:
    if i[0] == "push":
        q.insert(0, int(i[1]))
    elif i[0] == "pop":
        if len(q) == 0:
            print("-1")
        else:
            print(q.pop(len(q) - 1))
    elif i[0] == "size":
        print(len(q))
    elif i[0] == "empty":
        if len(q) == 0:
            print("1")
        else:
            print("0")
    elif i[0] == "back":
        if len(q) == 0:
            print("-1")
        else:
            print(q[0])
    else:
        if len(q) == 0:
            print("-1")
        else:
            print(q[len(q) - 1])
