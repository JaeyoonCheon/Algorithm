"""
    lv.3 보석 쇼핑

    1.  투포인터 구간 검색을 사용해 구간 내에 보석의 종류 개수가 총 종류 개수와 같은 경우 최소 길이의 구간을 탐색.
    2.  보석의 총 개수, 보석의 종류의 개수, 현재 구간의 보석의 종류별 개수를 저장하고 있어야 한다.
"""


def solution(gems):
    answer = [0, len(gems) - 1]

    start, end = 0, 0

    gemTotal = len(gems)
    gemCategoryTotal = len(set(gems))
    gemDict = {gems[0]: 1}

    while end < gemTotal:
        if len(gemDict) < gemCategoryTotal:
            end += 1

            if end == gemTotal:
                break

            gemDict[gems[end]] = gemDict.get(gems[end], 0) + 1
        else:
            if end - start < answer[1] - answer[0]:
                answer = [start, end]

            if gemDict[gems[start]] == 1:
                del gemDict[gems[start]]
            else:
                gemDict[gems[start]] -= 1

            start += 1

    return [answer[0] + 1, answer[1] + 1]


result = solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
