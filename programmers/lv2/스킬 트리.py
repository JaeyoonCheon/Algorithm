"""
    lv.2 스킬 트리
    
    1.  주어진 선행 스킬을 하나의 스택으로 생각하여 스킬트리 각각을 검사하면서 pop 순서에 맞지 않는 스킬을 발견하면
        +1을 제외하는 방식으로 구현.
"""

from collections import deque


def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        skillOrder = deque(skill[:])

        for s in tree:
            if s in skill and s != skillOrder.popleft():
                break
        else:
            answer += 1

    return answer
