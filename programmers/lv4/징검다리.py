"""
    lv.4 징검다리
    
    1.  조합을 사용해 완전탐색으로 풀이할 시 너무 많은 경우의 수가 발생. 이분 탐색 고려
    2.  범위와 기준을 설정
        기준 - 지점 사이의 거리의 최소값. 해당 거리를 기준으로 삭제할 바위 결정
        범위 - 0 ~ 끝 거리
    3.  이분 탐색을 진행하면서 이전 위치 ~ 현재 위치 사이의 거리가 기준보다 작을 때 해당 바위를 삭제하도록 한다.
"""


def solution(distance, rocks, n):
    answer = 0

    # 중요! 비교할 거리 중에 마지막 바위 ~ 끝 거리 사이의 거리를 비교하기 위해 총 길이를 위치로 추가
    rocks.append(distance)
    rocks.sort()

    # 바위 사이 거리의 최소값을 구해보자
    lo, hi = 0, distance

    while lo <= hi:
        # 초기값은 최대 거리의 절반부터
        mid = (lo + hi) // 2
        # 현재 설정한 거리가 최소가 되기 위해 조건에 맞지 않는 돌을 제거한 횟수
        removed = 0
        # 직전 바위의 위치
        previousPos = 0

        for rock in rocks:
            # 이전 바위와의 거리가 기준보다 작으면 현재 돌은 제거되어야 한다.
            if rock - previousPos < mid:
                removed += 1
            # 기준보다 넓으면 이전 위치 변경
            else:
                previousPos = rock

            if removed > n:
                break

        # 제거해야할 바위의 개수보다 많을 때, 기준 거리를 줄여보자
        if removed > n:
            hi = mid - 1
        else:
            answer = mid
            lo = mid + 1

    return answer
