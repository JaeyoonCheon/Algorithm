"""
1620번 나는야 포켓몬 마스터 이다솜

1.  딕셔너리 응용 문제.

2.  처음 시도에서 딕셔너리로 키-값 쌍을 만들어 저장 후 조회를 시도하였는데
    시간 초과가 발생했다.
    시간 초과의 주 원인은 값->키 조회 시 전 딕셔너리를 순회하는 탐색 구문 때문에
    시간이 초과한 것으로 생각된다.
    
3.  따라서, 키-값 쌍과 값-키 쌍을 저장하는 딕셔너리를 각각 만들어
    O(1) 시간에 탐색이 가능하도록 구현했다.
"""

import sys

N, M = map(int, input().split())

book_key = {}
book_val = {}

for i in range(N):
    val = sys.stdin.readline().rstrip()
    book_key[i + 1] = val
    book_val[val] = i + 1

for _ in range(M):
    find = sys.stdin.readline().rstrip()

    if find.isdigit():
        print(book_key.get(int(find)))
    else:
        print(book_val.get(find))
