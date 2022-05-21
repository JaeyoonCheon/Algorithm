"""
11399번 ATM

1.  각 사람 별 인출하는 데 걸리는 시간이 정해져 있고 모든 사람들이 인출 완료했을 때 최소 시간을
    구해야 하는 문제이므로, 인출하는데 시간이 적게 걸리는 사람부터 순서를 구성하면 최소 시간을
    구할 수 있을 것이다(그리디 문제).
    
2.  따라서, 사람들을 인출하는데 걸리는 시간 순서대로 재정렬해야 하므로 사람-인출시간 튜플 쌍을
    리스트에 저장해 인출시간으로 정렬했다.
    
3.  이후, 가장 앞(가장 적은 인출 시간)부터 차례대로 부분 합, 누적 합을 구하면 해결할 수 있다.
"""

N = int(input())

order = []
data = list(map(int, input().split()))

for i in range(N):
    order.append((data[i], i + 1))

order = sorted(order, key=lambda x: x[0])

sum = 0
partialSum = 0

for i in order:
    partialSum += data[i[1] - 1]
    sum += partialSum

print(sum)
