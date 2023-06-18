"""
    lv.2 순위 검색
    
    1.  단순히 4가지의 정보와 점수를 가지고 쿼리에 대해 검사하면 5억 가지 조건이 발생하므로 시간 효율성 하락.
    2.  그렇다면, 4가지의 정보로 -를 포함해 만들 수 있는 모든 경우를 저장해 놓고, 해당 경우와 일치하는 쿼리에 대해 기록된 점수들을 가져와
        몇 명의 점수가 기준을 넘겼는 지 확인한다.
"""


def simpleFind(info, query):
    data = [i.split() for i in info]
    queries = []

    for q in query:
        q = q.split()

        for i in range(3):
            q.remove("and")

        queries.append(q)

    answer = [0] * len(query)

    for i in range(len(queries)):
        q = queries[i]

        for info in data:
            for j in range(5):
                if q[j] == "-":
                    continue
                elif j == 4 and int(info[j]) >= int(q[j]):
                    answer[i] += 1
                elif info[j] != q[j]:
                    break

    return answer


import collections, itertools, bisect


def binFind(info, query):
    answer = []
    # 인적 정보 4가지로 만들 수 있는 모든 조합을 저장해놓는 딕셔너리
    people = collections.defaultdict(list)

    for i in info:
        # 인적 정보 배열
        person = i.split()
        # 위 배열에서 끝의 점수만 분리
        score = int(person.pop())
        # 인적 정보를 키로하는 딕셔너리에 점수 저장
        people["".join(person)].append(score)

        # -를 포함해 만들어낼 수 있는 조합들도 마찬가지로 딕셔너리에 저장
        for j in range(4):
            case = list(itertools.combinations(person, j))
            for c in case:
                people["".join(c)].append(score)

    # 각 조합에 저장된 점수들을 오름차순 정렬
    for i in people:
        people[i].sort()

    # 각각의 쿼리에 대해 조건/점수로 분해하고 검사
    for i in query:
        key = i.split()
        score = int(key.pop())
        key = "".join(key)
        key = key.replace("and", "").replace(" ", "").replace("-", "")

        # 해당 조건과 일치하는 조합에 저장된 점수들에서 인덱스(순위)를 이분탐색하여 가져옴
        answer.append(len(people[key]) - bisect.bisect_left(people[key], score))

    return answer


def solution(info, query):
    answer = []

    answer = binFind(info, query)

    return answer


solution(
    [
        "java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50",
    ],
    [
        "java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150",
        "- and - and - and chicken 100",
        "- and - and - and - 150",
    ],
)
