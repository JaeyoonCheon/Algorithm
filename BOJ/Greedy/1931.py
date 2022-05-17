"""
1931번 회의실 배정

1.  주어진 시작-끝 시간이 정해진 회의들을 가장 많이 할 수 있는 조합을 찾는 그리디 문제.

2.  가장 회의를 자주 할 수 있는 방법은 회의 시간이 빨리 끝나는 순서대로 회의를 정렬하여
    회의를 하는 것이다. 회의가 빨리 끝날수록 다른 회의를 시간 내에 더 할 수 있기 때문이다.
    
3.  따라서, 회의가 끝나는 시간대로 오름차순 정렬한 후, 다시 시작하는 시간대로 오름차순 정렬하면
    최대한 빨리 끝나는 회의 중 당장 할 수 있는 가장 빠른 회의를 선택하면 가장 많은 회의를 할 수 있다.
"""

N = int(input())

conf = list(list(map(int, input().split())) for _ in range(N))

sortedConf = sorted(conf, key=lambda k: (k[1], k[0]))

endTime = 0
count = 0

for s, e in sortedConf:
    if s >= endTime:
        count += 1
        endTime = e

print(count)
