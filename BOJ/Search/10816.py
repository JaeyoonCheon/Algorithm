"""
10816번 숫자 카드 2

1.  처음 구상한 풀이 방법
    모든 카드와 찾을 수를 리스트에 받아 찾길 원하는 수 하나하나마다
    list.count() 함수를 사용해 풀이하는 방법
    하지만 count()가 실행될 때 마다 O(N)의 시간복잡도가 추가될 것이므로
    다른 방법이 더 효율적일 것으로 생각되었다.
    
2.  카드를 입력 받을 때 마다 준비된 빈 리스트의 해당하는 인덱스에
    +1씩 해주어 카드의 갯수만을 저장하는 리스트를 만든다.
    -천만 ~ 천만 범위이므로 인덱스의 별도 조정을 위한 DIFF가 필요
"""

import sys

DIFF = 10000000

N = int(input())
cards = list(map(int, sys.stdin.readline().split()))
count = [0] * 20000002

for i in cards:
    count[i + DIFF] += 1

M = int(input())
forFind = list(map(int, input().split()))

for i in forFind:
    print(count[i + DIFF], end=" ")
