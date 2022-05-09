"""
프로그래머스
2020 카카오 인턴십 - 보석 쇼핑

1.  주어진 구간 중 모든 보석 종류가 한번씩 포함된 최소 구간을 찾는 문제.
    처음 시도로 구간의 처음부터 시작하여 그 점을 시작으로 주어진 구간의 끝까지 모든 구간을 찾았음
    답은 정확하게 나오나, 구간 최대가 10000 길이이므로 모든 구간을 탐색한다면 시간 복잡도가
    O(N^2)일 것이므로 효율적이지 못하다.
    
2.  투포인터 전략을 적용한다.
    투포인터란 두 개의 이동점을 유지하면서 어떤 문제의 조건을 만족한다면
    앞의 포인터를 당기고, 만족하지 않는다면 뒤의 포인터를 밀어 조건을 만족할 때 까지 반복한다.
    해당 전략을 적용하면 시간 효율이 좋아진다.
    하지만 result = list(map(lambda x: x in gems[scopeStart : scopeEnd + 1], allGems)) 구문으로
    구간의 모든 보석 포함 여부를 조사하였는데, 서로 다른 보석의 갯수가 많아진다면 검사하는 시간이
    O(N)이 발생하므로 이 부분의 개선이 필요하다.
    
3.  
"""


def solution(gems):
    answer = []

    allGemsLength = len(set(gems))

    minLength = len(gems) + 1
    scopeStart, scopeEnd = 0, 0
    currentGems = {}

    # 끝 포인터가 끝까지 도달한다면 시작 포인터를 당기는 동작밖에 없다.
    # 시작 포인터는 내부 loop에서 움직이므로, 끝 포인터가 끝에 도달하면 큰 loop의 동작은 끝난다.
    while scopeEnd < len(gems):
        # 현재 구간에 없었다면 현재 구간에 존재한다고 체크(키:gems[scopeEnd] / 값:1)
        if gems[scopeEnd] not in currentGems:
            # 현재 구간에 존재하는 보석의 개수 1 증가
            currentGems[gems[scopeEnd]] = 1
        # 끝 포인터 위치의 보석이 구간 내에 존재하면
        else:
            currentGems[gems[scopeEnd]] += 1

        # 체크를 했다면 끝 포인터를 뒤로 1칸 증가
        scopeEnd += 1

        # 만약, 현재 구간의 보석 종류가 모든 보석 종류의 수와 같다면
        if len(currentGems) == allGemsLength:
            # 시작 포인터를 끝 포인터보다 작은 범위에서 민다
            while scopeStart < scopeEnd:
                # 현재 구간에 1개보다 많은 시작 포인터 위치의 보석 종류가 있을 때
                if currentGems[gems[scopeStart]] > 1:
                    currentGems[gems[scopeStart]] -= 1
                    scopeStart += 1
                # 현재 구간에 단 1개의 시작 포인터 위치의 보석 종류가 있을 때
                # 모든 보석 종류를 가지기 위해서는 시작 위치에서 더 밀어낼 수 없으므로
                # 해당 케이스에서 최소 구간일 경우에 최소 구간을 갱신
                elif minLength > scopeEnd - scopeStart:
                    minLength = scopeEnd - scopeStart
                    answer = [scopeStart + 1, scopeEnd]
                    break
                else:
                    break

    return answer


inputData = ["a", "b", "c", "b", "c", "d", "f", "d", "b", "e", "g", "e", "a"]

print(solution(inputData))
