"""
    lv.3 징검다리 건너기
    
    1.  이분 탐색을 활용한 범위 줄이기 방식으로, 바위를 건널 사람의 인원을 기준으로 설정하고 이분탐색.
    2.  해당 인원이 k제한인 바위들을 건널 수 있다면 더 늘려보고, 못 건넌다면 줄여 이분 탐색.
"""


def check(stones, k, n):
    skip = 0
    for stone in stones:
        # 카운트 n 이하인 바위가 연속 k개 이하인지 체크
        if stone < n:
            skip += 1
            if skip >= k:
                return False
        else:
            skip = 0

    return True


def solution(stones, k):
    answer = 0

    # 기준은 건널 사람의 인원 수.
    lo, hi = 0, max(stones)

    while lo <= hi:
        mid = (lo + hi) // 2

        # 건널수 있다면,, 인원 수를 더 늘려보자
        if check(stones, k, mid):
            answer = mid
            lo = mid + 1
        else:
            hi = mid - 1

    return answer
