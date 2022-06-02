"""
1918번 후위 표기식

1.  중위 표기식으로 주어진 수식을 후위표기식으로 변환하는 문제.

2.  중위 표기식(infix) -> 후위 표기식(postfix)
    1)  피연산자는 만나는 즉시 출력
    2)  스택이 비어있을 때 연산자를 만나면 스택에 저장
    3)  스택의 top이 현재 연산자보다 우선순위가 낮을 때 까지 스택에 저장된 연산자들을
        top부터 pop하여 출력. 단, (를 만나면 정지
    4)  )를 입력받으면 (가 스택에서 나올 때 까지 출력. 괄호는 출력하지 않고 스택에서 삭제
    5)  모든 수식을 순회했다면, 스택에 저장된 연산자들을 모두 pop하여 출력
"""

expression = input().rstrip()

priority = {"+": 0, "-": 0, "*": 1, "/": 1, "(": 2, ")": 2}

stack = []
top = -1

for ch in expression:
    if ch not in priority.keys():
        print(ch, end="")
    else:
        if ch == ")":
            while True:
                curr = stack.pop()
                top -= 1
                if curr == "(":
                    break
                else:
                    print(curr, end="")
        else:
            if not stack:
                stack.append(ch)
                top += 1
                continue

            while True:
                peek = stack[top]

                if not stack or peek == "(" or priority[peek] < priority[ch]:
                    stack.append(ch)
                    top += 1
                    break

                print(stack.pop(), end="")
                top -= 1

                if not stack:
                    stack.append(ch)
                    top += 1
                    break

while stack:
    print(stack.pop(), end="")
