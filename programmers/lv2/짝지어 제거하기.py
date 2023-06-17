"""
    lv.2 짝지어 제거하기
    
    1.  정규표현식 등으로 계속 반복해 쌍이 되는 문자를 제거해 나가도 동작은 할 수 있다. 그러나 1000000 길이의 문자열이 최악의 경우
        nlogn이 소요될 수 있으므로, 입력 시 바로 처리가 되어 n시간에 동작하도록 해야 한다.
    2.  따라서, 스택을 이용해 문자열을 하나씩 받아오며 top과 동일한 문자일 경우 스택에서 제거하도록 작성.
"""


def solution(s):
    answer = -1

    stack = []
    top = -1

    for c in s:
        if top == -1:
            stack.append(c)
            top += 1
        elif stack[top] != c:
            stack.append(c)
            top += 1
        else:
            stack.pop()
            top -= 1

    if top == -1:
        answer = 1
    else:
        answer = 0

    return answer


solution("baabaa")
