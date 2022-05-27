"""
17219번 비밀번호 찾기

1.  입출력 양이 100000이지만 딕셔너리를 이용하여 간단하게 해결 가능
"""

import sys

N, M = map(int, sys.stdin.readline().split())

DB = {}

for _ in range(N):
    id, pw = sys.stdin.readline().split()
    id.rstrip()
    pw.rstrip()

    DB[id] = pw

for _ in range(M):
    id = sys.stdin.readline().rstrip()

    print(DB[id])
