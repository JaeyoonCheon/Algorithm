"""
1043번 거짓말

1.  진실을 아는 사람들의 목록과 파티에 참석하는 사람들을 모두 알고 있을때 거짓말을 할 수 있는 파티의 수를
    구하는 문제. 파티의 시간 순서는 고려하지 않고 진실을 아는 사람들이 진실을 같은 파티에 참석한 사람들에게
    전파할 수 있고 전파받은 사람들의 행동 또한 동일하게 수행된다.
    
2.  따라서, 모든 전파가 이루어지고 난 뒤 진실을 모르는 사람만 있는 파티의 수만 원하기 때문에
    그래프 탐색이나 집합 원리를 사용해야 할 것으로 보임
    
3.  해당 풀이는 BFS를 이용해 파티를 노드로, 각 참석자가 다른 파티에 참석하는 관계를 간선으로 간주하여
    BFS를 수행하여 해결했다.
    
4.  쉬운 풀이로 Union-Find 방법(Disjoint Set)을 응용하면 좋을 것으로 보인다.
"""

import collections

N, M = map(int, input().split())

known = list(map(int, input().split()))
known.pop(0)

participate = [list(map(int, input().split())) for _ in range(M)]

for event in participate:
    event.pop(0)

party = [False] * M

q = collections.deque()

for idx, person in enumerate(known):
    q.append(person)

known = []


def BFS():
    if q:
        while q:
            who = q.popleft()
            known.append(who)

            for i in range(M):
                if who in participate[i] and not party[i]:
                    party[i] = True
                    for people in participate[i]:
                        if people not in known and people not in q:
                            q.append(people)


BFS()

count = 0

for i in party:
    if not i:
        count += 1

print(count)
