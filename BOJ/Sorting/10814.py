"""
10814번 나이순 정렬

1.  이중 정렬 문제.

2.  이중 정렬 시, 두 번째 정렬 조건이 입력된 순서이므로 입력받을 때 마다 그 입력 값에
    인덱스를 부여해 주어야 한다.
    
3.  파이썬의 내장 정렬 함수 sorted()에 람다식을 응용한 정렬 키를 나이/입력 순서의 2개 키를
    부여하여 오름차순으로 이중 정렬해 주었다.
"""

N = int(input())

people = [list(input().split()) for _ in range(N)]

for i in range(N):
    people[i][0] = int(people[i][0])
    people[i].append(i)

sortedPeople = sorted(people, key=lambda x: (x[0], x[2]))

for i in range(N):
    print(f"{sortedPeople[i][0]} {sortedPeople[i][1]}")
