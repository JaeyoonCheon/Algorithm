"""
    lv.3 불량 사용자
    
    1.  밴 규칙 하나하나에 대한 아이디들의 조합 개수를 검사
    2.  정규표현식 형태로 밴 규칙을 변환한 뒤, 각각의 규칙에 대해 가능한 아이디 조합을 검사.
    3.  조합은 순열로 구성하거나, dfs & 비트마스킹을 사용해도 됨
    4.  현재 풀이는 정규식 표현을 하나로 합친 뒤 아이디 조합을 하나로 결합한 문자열과 비교한 풀이.
"""

import re, itertools


def solution(user_id, banned_id):
    answer = 0

    bannedRegex = " ".join(banned_id).replace("*", ".")
    cases = []

    for i in itertools.permutations(user_id, len(banned_id)):
        if re.fullmatch(bannedRegex, " ".join(i)):
            cases.append("".join(sorted(i)))

    answer = len(set(cases))

    return answer


solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])
