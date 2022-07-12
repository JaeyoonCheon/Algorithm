"""
1202번 보석 도둑

1.  일단 가장 중요한 논리는 보석의 가치 순으로 정렬한 뒤 가장 큰 가치를 가진 보석을
    넣을 수 있는 가장 작은 크기의 배낭에 넣는다면 최적의 결과값이 나올 것이라는 것이며
    곧 그리디 문제로 해석할 수 있겠다.
    
2.  넣을 수 있는 가장 작은 크기의 배낭을 찾는 부분을 이진 탐색으로 수행하려고 했으나,
    O(NK) 선형시간에 수행되어 시간 제한에 풀이하지 못했다.
    
3.  따라서 시도해 볼 수 있는 것은 O(logNK)시간에 해결할 수 있도록 보석-가방을 한번에 처리하고
    그것을 heapq와 같은 자료구조로 처리하는 것이다.
    
4.  보석-가방을 한 리스트에 무게 순으로 정렬한 뒤,
    앞에서부터 하나씩 뽑아 보석일 경우 우선순위 큐에 가치를 역으로 해 저장하고,
    가방일 경우에 우선순위 큐에서 가장 앞에 있는 가치가 음으로 최대인 것을 뽑아 다시 역을 취한 뒤
    총 가치에 더해준다.
    이것은 앞서 무게 순으로 정렬하여 처리하기 때문에 가방을 뽑았을 때 우선순위 큐에는
    뽑은 가방의 무게보다 같거나 작은 무게의 보석만이 들어있는데 그 보석등은 가치의 역으로 저장되어있기 때문에
    pop할 시 뽑은 가방의 무게보다 같거나 작은 무게를 가진 최대 가치의 보석을 뽑게 된다.
"""

import heapq
import sys, bisect

N, K = map(int, input().split())

items = []

for _ in range(N):
    weight, value = map(int, sys.stdin.readline().split())
    items.append((weight, value))

for _ in range(K):
    size = int(sys.stdin.readline())
    items.append((size, 2000000))

items.sort()
q = []
allValue = 0

for item in items:
    if item[1] != 2000000:
        heapq.heappush(q, -item[1])
    else:
        if q:
            value = -heapq.heappop(q)
            allValue += value

print(allValue)

# gems = []

# for _ in range(N):
#     gems.append(tuple(map(int, sys.stdin.readline().split())))

# bags = []

# for _ in range(K):
#     bags.append(int(sys.stdin.readline()))

# sortedGems = sorted(gems, key=lambda x: (-x[1], x[0]))
# sortedBags = sorted(bags)


# def findIdx(weight):
#     global allValue
#     idx = bisect.bisect_left(sortedBags, weight)

#     if idx >= len(sortedBags):
#         return
#     else:
#         allValue += value
#         sortedBags.pop(idx)


# allValue = 0

# for gem in sortedGems:
#     if not sortedBags:
#         break
#     weight, value = gem[0], gem[1]
#     idx = findIdx(weight)


# print(allValue)
