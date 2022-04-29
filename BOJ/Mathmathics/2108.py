"""
2108번 통계학
"""

import sys

N = int(sys.stdin.readline())

lists = [int(sys.stdin.readline()) for _ in range(N)]

lists.sort()

print(round(sum(lists) / N))
print(lists[N // 2])


sets = set(lists)
sortedSets = sorted(sets)
counts = [0] * len(sortedSets)

for i in lists:
    counts[sortedSets.index(i)] += 1

first, second = 0, 0
for i in range(len(counts)):
    if counts[i] == max(counts):
        second = first
        if first == 0:
            second = first = i
        else:
            first = i
            break

if sortedSets[first] <= 0 and sortedSets[second] <= 0:
    print(sortedSets[first])
elif sortedSets[first] >= 0 and sortedSets[second] <= 0:
    print(sortedSets[first])
else:
    print(sortedSets[second])

print(max(lists) - min(lists))
