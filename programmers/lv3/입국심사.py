"""
    lv.3 입국심사
    
    1.  입력값이 10억으로 아주 크기 때문에 logN을 고려해야 한다. 따라서 이분 탐색을 우선 고려.
    2.  최소 작업 우선 스케쥴링과 같이 각각의 사람이 각 심사대에서 걸리는 소요 시간을 구할 수는 있을것이나,
        최적의 시간임을 보장할 수는 없다.
    3.  관점을 바꿔 심사에 걸리는 총 시간을 최소 ~ 최대로 검사해보면 이분 탐색으로 접근 가능.
"""


def solution(n, times):
    answer = 0

    # 총 심사 시간의 범위는 1 ~ 최대 시간이 걸리는 심사대로 n명이 심사받는 시간의 합
    lo = 1
    hi = max(times) * n

    while lo <= hi:
        # 총 걸릴 것으로 예상되는 시간
        mid = (lo + hi) // 2

        canPass = 0

        # 각 심사대에서 총 시간을 나눈 비율(검사할 수 있는 사람의 수. 소수로 나올 수 있다)
        for time in times:
            canPass += mid // time

            if canPass >= n:
                break

        # 총 예상시간으로 mid가 산정되었을 때 n명 이상 검사가능하다면
        if canPass >= n:
            # 더 적은 총 예상시간을 찾아보자
            answer = mid
            hi = mid - 1
        # n명 검사가 불가능하다면
        else:
            # 더 많은 총 예상시간을 찾아보자
            lo = mid + 1

    return answer
