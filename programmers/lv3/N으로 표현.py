"""
    lv.3 N으로 표현
    
    1.  DP를 사용해 bottom-up으로 구성해나가는 문제.
    2.  N이라는 수를 몇 번 사용한 연산이라는 것을 DP의 기준으로 세우고 사칙연산.
"""


def solution(N, number):
    answer = -1

    # 연산
    dp = [set() for _ in range(9)]

    for i in range(1, 9):
        case = dp[i]
        # N을 자리수를 늘려 만든 수 추가 (5, 55, 555 ...)
        case.add(int(str(N) * i))

        # 현재 연산은 이전 연산 결과들 간의 사칙연산의 결과들(6번째 연산 = 연산 1 X 연산 5, 연산 2 X 연산 4...)
        for j in range(1, i):
            # k, l 이전 연산 횟수들로 만들 수 있는 모든 조합에 대해 순회
            for k in dp[j]:
                for l in dp[i - j]:
                    case.add(k + l)
                    case.add(k - l)
                    case.add(k * l)
                    if l != 0 and k != 0:
                        case.add(k // l)

        # 해당 회차의 결과에 목표 값이 있으면 종료
        if number in case:
            answer = i
            break

    return answer
