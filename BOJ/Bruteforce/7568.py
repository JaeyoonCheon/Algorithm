"""
7568번 덩치

1.  주어진 정보는 각 사람들의 몸무게/키 정보이다.
    이 때, 각 사람들의 등수를 구별하는 기준은 몸무게/키 모두가 크면 등수가 더 높고
    몸무게/키 모두가 더 낮아야 등수가 낮다.
    이외에 몸무게가 큰데 키가 작거나 몸무게가 작은데 키가 작은 경우엔 등수가 동일하다.
    
2.  빠른 비교와 동일 등수가 존재할 때 하위 등수가 밀려나는 것을 고려하기 위해
    1명 씩 삽입하면서 등수를 계산하도록 했다.
    삽입한 사람과 기존 사람들을 비교하면서, 등수가 낮다면 삽입한 사람의 등수를 1 증가시키고,
    등수가 높으면 비교 대상이 된 사람의 등수를 증가시킨다.
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
