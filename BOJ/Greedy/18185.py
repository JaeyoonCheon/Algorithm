"""
18185번 라면 사기(small)

1.  첫 접근법으로,
    1)의 지시로 공장 하나에 3,
    2)의 지시로 공장 둘에 5,
    3)의 지시로 공장 셋에 7의 비용이 소모되므로 각 지시의 공장 하나 당 효율이 3/2.5/2.033... 이라는 점에 착안해
    무조건 인덱스 당 공장을 많이 포함하는 지시가 효율적일 것으로 생각하여 첫 공장부터 방문하면서 i/i+1/i+2 인덱스에 대해 3개, 2개, 1개를 구매하는 방식으로 접근했다.
    하지만 이 방법은 무조건 3, 2개를 사는 지시가 결과적으로 많아질 것이라는 보장을 하지 못한다는 것을 발견했다.
    
2.  반대로 생각하면 현재 사려는 공장 i에 대해 i-1, i-2에서 산 "비효율적인" 지시들을 더 많이 살 수 있는 "효율적인" 지시로 바꿔주는 것이
    결과적으로 가장 많은 효율적 지시를 할 수 있음을 알 수 있다.
    따라서 i번째 공장에 있을 때 해야하는 절차로 동일하게 3가지가 있다.
    a)  i-1에서 1)로 샀던 지시를 현재 i에서의 라면을 포함한 2)로 대체해주는것.
    b)  i-2에서 2)로 샀던 지시를 현재 i에서의 라면을 포함한 3)으로 대체해주는것.
    c)  a), b)를 수행하고 남은 라면은 2)~3)으로 연계해서 살 수 없으므로 1)의 지시로 모두 개별 구매하는것.
    
    a), b) 이외의 경우는 a), b)에서 파생되는 경우로 모두 위의 과정에서 계산되므로 고려할 필요가 없다.
"""

N = int(input())

factory = list(map(int, input().split()))

totalFee = 0

op = [[0, 0, 0] for _ in range(N)]

for i in range(N):
    if factory[i] == 0:
        continue
    if i == 0:
        op[i][0] = factory[i]
        continue

    toBuy = factory[i]

    if op[i - 1][0]:
        toReplace = min(op[i - 1][0], toBuy)
        op[i - 1][0] -= toReplace
        op[i - 1][1] += toReplace

        toBuy -= toReplace
    if op[i - 2][1]:
        toReplace = min(op[i - 2][1], toBuy)
        op[i - 2][1] -= toReplace
        op[i - 2][2] += toReplace

        toBuy -= toReplace
    if toBuy:
        op[i][0] += toBuy
        toBuy = 0

for count in op:
    totalFee += count[0] * 3 + count[1] * 5 + count[2] * 7

print(totalFee)
