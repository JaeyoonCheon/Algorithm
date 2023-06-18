"""
    lv.1 모의고사

    1.  나올 수 있는 답의 가지수가 정해져 있으므로 완전 탐색을 진행
"""


def solution(answers):
    answer = []

    score = {1: 0, 2: 0, 3: 0}

    mark1 = [1, 2, 3, 4, 5]
    mark2 = [2, 1, 2, 3, 2, 4, 2, 5]
    mark3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i, v in enumerate(answers):
        if v == mark1[i % len(mark1)]:
            score[1] += 1
        if v == mark2[i % len(mark2)]:
            score[2] += 1
        if v == mark3[i % len(mark3)]:
            score[3] += 1

    maxScore = max(list(score.values()))
    answerTuple = list(filter(lambda x: x[1] == maxScore, list(score.items())))
    answer = list(map(lambda x: x[0], answerTuple))

    return answer


result = solution([1, 3, 2, 4, 2])
print(result)
