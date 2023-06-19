"""
    lv.4 도둑질
    
    1.  dp를 i번째 집까지 털었을 때 가장 큰 금액으로 정의했을 때 풀이가 편해지는 문제.
    2.  총 길이가 홀수일 경우, 마지막 집을 털 수 없는 경우가 생기므로, 두번째 집부터 터는 경우의 수도 한번 더 고려해야 함.
"""


def solution(money):
    answer = 0

    # dp = i번째 집까지 털었을 때 만들 수 있는 가장 큰 금액

    # 첫번째 집을 털었을 경우 두번째 집은 털지 못한다.
    dp1 = [0] * len(money)
    dp1[0] = dp1[1] = money[0]

    for i in range(2, len(money) - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])

    # 두번째 집을 털었을 경우 첫번째 집은 털지 못한다.
    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]

    for i in range(2, len(money)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])

    answer = max(max(dp1), max(dp2))

    return answer
