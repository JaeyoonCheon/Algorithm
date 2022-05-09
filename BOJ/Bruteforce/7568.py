"""
7568번 덩치
"""

N = int(input())
people = []

for i in range(N):
    weight, height = map(int, input().split())
    rank = 1
    for j in people:
        if j[0] > weight and j[1] > height:
            rank = rank + 1
        elif j[0] < weight and j[1] < height:
            j[2] += 1
        else:
            continue
    people.append([weight, height, rank])

for i in people:
    print(i[2], end=" ")
