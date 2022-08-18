"""
2568번 전깃줄 - 2

1.  문제를 잘 살펴보면 여러 개의 연결된 전깃줄 중 몇 개를 없애 '최대 개수의 연결된 전깃줄'을
    만드는 경우의 수를 찾는 문제이다. 이 때, 교차하는 전깃줄을 없애야 하는데 교차한다는 것은
    정렬된 A에 연결된 전깃줄 기준으로 이전 전깃줄이 B에 연결된 위치보다 현재 전깃줄이 B에 연결된 위치가
    더 작은 경우를 의미하는 것으로 볼 수 있다.

2.  따라서 전깃줄을 A 전봇대 기준으로 정렬하면, 각각의 전깃줄이 B에 연결된 위치가 증가되는 순서대로 만들 수 있는
    부분 수열을 찾는 문제가 된다. 따라서, LIS(최대 증가 부분수열)을 풀이하는 방식으로 해결할 수 있게 된다!

3.  DP를 이용한 LIS 풀이법으로 풀어도 좋겠지만, 전깃줄의 개수가 100000개이기 때문에
    더 효율적인 풀이인 BOJ 12015번의 이진탐색을 활용한 방법으로 접근했다.

4.  q[idx]는 LIS 길이 idx에서 적용할 수 있는 최소의 값을 의미한다.
    따라서 정렬된 전깃줄의 연결된 위치를 순회하며 q의 마지막 값(현재 LIS의 끝 위치의 값)보다 값이 크다면,
    LIS가 증가할 수 있으므로 q의 끝에 삽입하면 된다.
    그리고 q의 마지막값보다 현재 값이 같거나 작을 경우 현재까지의 LIS에서 현재 값이 위치할 수 있는 자리를
    이진 탐색 lower bound로 찾아내 해당 위치를 대체하도록 한다.

5.  이 때 만들어낸 LIS는 정확한 LIS가 아니며 LIS의 길이를 알아내기 위해 값들의 대소만을 비교하는 표이기 때문에
    값들을 삽입할 때 해당 값이 LIS의 어느 위치에 적용되는 지 그 인덱스를 기록해 놓는다.
    이후, LIS길이만큼 저장된 모든 인덱스들을 순회하며 뒤에서부터 LIS길이와 일치하는 인덱스를 가진 전깃줄을
    출력하고 LIS길이를 -1 줄이는 과정을 반복하면 실제 LIS중 하나를 얻을 수 있다.
    우리가 원하는 것은 LIS에 포함되지 않는 제거해야 하는 전깃줄이므로 뒤에서부터 LIS길이와 일치하지 않는 
    인덱스를 만날 경우 그 인덱스를 가지는 전깃줄의 A위치를 저장 후 정렬, 출력하면 된다.
"""

import sys, collections, bisect

N = int(sys.stdin.readline())

lines = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

lines.sort(key=lambda poll: poll[0])

q = collections.deque()
index = collections.deque()
q.append(lines[0][1])
index.append(0)

for line in lines[1:]:
    length = len(q)
    endPoint = line[1]

    if endPoint > q[length - 1]:
        q.append(endPoint)
        length = len(q)
        index.append(length - 1)
    else:
        idx = bisect.bisect_left(q, endPoint)
        q[idx] = endPoint
        index.append(idx)

print(N - len(q))

currentPos = len(q) - 1
result = []

for i in range(len(index) - 1, -1, -1):
    if currentPos == index[i]:
        currentPos -= 1
    else:
        result.append(lines[i][0])

result.sort()

for i in result:
    print(i, end=" ")
