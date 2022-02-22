"""
14501번 퇴사

1. 백트래킹 이용
경우의 수는 2가지이다.
1) 해당 일자에서 상담을 받아 상담 일자 만큼 시간을 소요하여 수입을 얻는 경우
2) 해당 일자에서 상담을 받지 않아 하루를 쉬고 수입도 얻지 않는 경우
"""


def findMaxIncome(N, T, P, day, currIncome):
    global maxIncome

    if day > N + 1:
        return
    if day == N + 1:
        if maxIncome < currIncome:
            maxIncome = currIncome
        return
    else:
        nextDay = day + T[day]
        nextIncome = currIncome + P[day]
        findMaxIncome(N, T, P, nextDay, nextIncome)
        findMaxIncome(N, T, P, day + 1, currIncome)


maxIncome = 0
N = int(input())
T = [-1]
P = [-1]

for _ in range(N):
    t_i, p_i = map(int, input().split())
    T.append(t_i)
    P.append(p_i)

findMaxIncome(N, T, P, 1, 0)

print(maxIncome)
