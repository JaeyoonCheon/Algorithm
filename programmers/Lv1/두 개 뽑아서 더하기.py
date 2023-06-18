"""
    lv.1 두 개 뽑아서 더하기

    1.  모든 수 조합 계산
    2.  중복 제거
    3.  오름차순 정렬
"""


def solution(numbers):
    answer = set()

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.add(numbers[i] + numbers[j])

    answer = list(answer)
    answer.sort()

    return answer
